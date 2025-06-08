# Corporate proxy

Third-party integrations

# Corporate proxy configuration

Copy page

This page covers how to configure Claude Code to work with corporate proxy
servers, including environment variable configuration, authentication, and
SSL/TLS certificate handling.

##

​

Overview

Claude Code supports standard HTTP/HTTPS proxy configurations through
environment variables. This allows you to route all Claude Code traffic
through your organization’s proxy servers for security, compliance, and
monitoring purposes.

##

​

Basic proxy configuration

###

​

Environment variables

Claude Code respects standard proxy environment variables:

    
    
    # HTTPS proxy (recommended)
    export HTTPS_PROXY=https://proxy.example.com:8080
    
    # HTTP proxy (if HTTPS not available)
    export HTTP_PROXY=http://proxy.example.com:8080
    

Claude Code currently does not support the `NO_PROXY` environment variable.
All traffic will be routed through the configured proxy.

Claude Code does not support SOCKS proxies.

##

​

Authentication

###

​

Basic authentication

If your proxy requires basic authentication, include credentials in the proxy
URL:

    
    
    export HTTPS_PROXY=http://username:password@proxy.example.com:8080
    

Avoid hardcoding passwords in scripts. Use environment variables or secure
credential storage instead.

For proxies requiring advanced authentication (NTLM, Kerberos, etc.), consider
using an LLM Gateway service that supports your authentication method.

###

​

SSL certificate issues

If your proxy uses custom SSL certificates, you may encounter certificate
errors.

Ensure that you set the correct certificate bundle path:

    
    
    export SSL_CERT_FILE=/path/to/certificate-bundle.crt
    export NODE_EXTRA_CA_CERTS=/path/to/certificate-bundle.crt
    

##

​

Additional resources

  * [Claude Code settings](/en/docs/claude-code/settings)
  * [Environment variables reference](/en/docs/claude-code/settings#environment-variables)
  * [Troubleshooting guide](/en/docs/claude-code/troubleshooting)

Was this page helpful?

YesNo

[Google Vertex AI](/en/docs/claude-code/google-vertex-ai)[LLM
gateway](/en/docs/claude-code/llm-gateway)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)[discord](https://www.anthropic.com/discord)

