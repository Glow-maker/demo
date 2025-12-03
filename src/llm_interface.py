"""
LLM Interface Module
Provides a unified interface for different LLM providers
"""

import os
from typing import Dict, List, Optional, Any
from enum import Enum


class LLMProvider(Enum):
    """Supported LLM providers"""
    OPENAI = "openai"
    QWEN = "qwen"
    GLM = "glm"
    ANTHROPIC = "anthropic"
    LOCAL = "local"


class LLMInterface:
    """
    Unified interface for interacting with different LLM providers
    """
    
    def __init__(
        self,
        provider: str = "openai",
        api_key: Optional[str] = None,
        model: str = "gpt-4",
        base_url: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 2000
    ):
        """
        Initialize LLM interface
        
        Args:
            provider: LLM provider name (openai, qwen, glm, etc.)
            api_key: API key for the provider
            model: Model name to use
            base_url: Custom API base URL (optional)
            temperature: Temperature for generation (0-1)
            max_tokens: Maximum tokens to generate
        """
        self.provider = provider.lower()
        self.api_key = api_key or os.getenv(f"{provider.upper()}_API_KEY")
        self.model = model
        self.base_url = base_url
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        self._client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the appropriate LLM client based on provider"""
        if self.provider == LLMProvider.OPENAI.value:
            try:
                from openai import OpenAI
                self._client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url
                )
            except ImportError:
                raise ImportError("OpenAI package not installed. Install with: pip install openai")
        
        elif self.provider == LLMProvider.ANTHROPIC.value:
            try:
                from anthropic import Anthropic
                self._client = Anthropic(api_key=self.api_key)
            except ImportError:
                raise ImportError("Anthropic package not installed. Install with: pip install anthropic")
        
        elif self.provider in [LLMProvider.QWEN.value, LLMProvider.GLM.value]:
            # These often use OpenAI-compatible APIs
            try:
                from openai import OpenAI
                self._client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url or self._get_default_base_url()
                )
            except ImportError:
                raise ImportError("OpenAI package not installed. Install with: pip install openai")
        
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")
    
    def _get_default_base_url(self) -> Optional[str]:
        """Get default base URL for provider"""
        urls = {
            LLMProvider.QWEN.value: "https://dashscope.aliyuncs.com/compatible-mode/v1",
            LLMProvider.GLM.value: "https://open.bigmodel.cn/api/paas/v4"
        }
        return urls.get(self.provider)
    
    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> str:
        """
        Generate text using the LLM
        
        Args:
            prompt: User prompt
            system_prompt: System prompt (optional)
            temperature: Override default temperature
            max_tokens: Override default max_tokens
            
        Returns:
            Generated text
        """
        temp = temperature if temperature is not None else self.temperature
        max_tok = max_tokens if max_tokens is not None else self.max_tokens
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        if self.provider == LLMProvider.ANTHROPIC.value:
            response = self._client.messages.create(
                model=self.model,
                max_tokens=max_tok,
                temperature=temp,
                messages=messages
            )
            return response.content[0].text
        else:
            # OpenAI-compatible API
            response = self._client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temp,
                max_tokens=max_tok
            )
            return response.choices[0].message.content
    
    def batch_generate(
        self,
        prompts: List[str],
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> List[str]:
        """
        Generate text for multiple prompts
        
        Args:
            prompts: List of user prompts
            system_prompt: System prompt (optional)
            temperature: Override default temperature
            max_tokens: Override default max_tokens
            
        Returns:
            List of generated texts
        """
        results = []
        for prompt in prompts:
            result = self.generate(prompt, system_prompt, temperature, max_tokens)
            results.append(result)
        return results
    
    def generate_with_json(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Generate JSON output using the LLM
        
        Args:
            prompt: User prompt
            system_prompt: System prompt (optional)
            temperature: Override default temperature
            
        Returns:
            Parsed JSON dictionary
        """
        import json
        import re
        
        # Add JSON formatting instruction to prompt
        json_instruction = "\n\nPlease respond with valid JSON format only."
        full_prompt = prompt + json_instruction
        
        response = self.generate(full_prompt, system_prompt, temperature)
        
        # Extract JSON from response (handle cases with markdown code blocks)
        json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # Try to find JSON object directly
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
            else:
                json_str = response
        
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON from LLM response: {e}\nResponse: {response}")


# Convenience functions
def create_llm(
    provider: str = "openai",
    api_key: Optional[str] = None,
    model: Optional[str] = None,
    **kwargs
) -> LLMInterface:
    """
    Create an LLM interface with sensible defaults
    
    Args:
        provider: LLM provider name
        api_key: API key
        model: Model name (uses provider default if not specified)
        **kwargs: Additional arguments for LLMInterface
        
    Returns:
        LLMInterface instance
    """
    # Default models for each provider
    default_models = {
        LLMProvider.OPENAI.value: "gpt-4",
        LLMProvider.QWEN.value: "qwen-plus",
        LLMProvider.GLM.value: "glm-4",
        LLMProvider.ANTHROPIC.value: "claude-3-opus-20240229"
    }
    
    if model is None:
        model = default_models.get(provider.lower(), "gpt-4")
    
    return LLMInterface(provider=provider, api_key=api_key, model=model, **kwargs)
