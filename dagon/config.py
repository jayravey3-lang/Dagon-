"""
Configuration module for Dagon AI
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    
    # Model configuration
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt2")
    MAX_HISTORY = int(os.getenv("MAX_HISTORY", "5"))
    MAX_MEMORY_SIZE = int(os.getenv("MAX_MEMORY_SIZE", "100"))
    
    # API configuration
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "5000"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Personality defaults
    DEFAULT_HELPFULNESS = float(os.getenv("DEFAULT_HELPFULNESS", "0.9"))
    DEFAULT_CREATIVITY = float(os.getenv("DEFAULT_CREATIVITY", "0.7"))
    DEFAULT_EMPATHY = float(os.getenv("DEFAULT_EMPATHY", "0.8"))
    DEFAULT_HUMOR = float(os.getenv("DEFAULT_HUMOR", "0.6"))
    DEFAULT_FORMALITY = float(os.getenv("DEFAULT_FORMALITY", "0.5"))


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    MODEL_NAME = "gpt2"


def get_config(environment="development"):
    """
    Get configuration object
    
    Args:
        environment (str): Environment name
        
    Returns:
        Config: Configuration object
    """
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig
    }
    
    return configs.get(environment, DevelopmentConfig)
