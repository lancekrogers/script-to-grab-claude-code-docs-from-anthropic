# Overview

Claude Code

# Claude Code overview

Learn about Claude Code, an agentic coding tool made by Anthropic. Currently
in beta as a research preview.

Claude Code is an agentic coding tool that lives in your terminal, understands
your codebase, and helps you code faster through natural language commands. By
integrating directly with your development environment, Claude Code
streamlines your workflow without requiring additional servers or complex
setup.

    
    
    npm install -g @anthropic-ai/claude-code
    

Claude Code’s key capabilities include:

  * Editing files and fixing bugs across your codebase
  * Answering questions about your code’s architecture and logic
  * Executing and fixing tests, linting, and other commands
  * Searching through git history, resolving merge conflicts, and creating commits and PRs
  * Works with [Amazon Bedrock and Google Vertex AI](/en/docs/claude-code/bedrock-vertex) for enterprise deployments

**Research preview**

Code is in beta as a research preview. We’re gathering developer feedback on
AI collaboration preferences, which workflows benefit most from AI assistance,
and how to improve the agent experience.

This early version will evolve based on user feedback. We plan to enhance tool
execution reliability, support for long-running commands, terminal rendering,
and Claude’s self-knowledge of its capabilities in the coming weeks.

Report bugs directly with the `/bug` command or through our [GitHub
repository](https://github.com/anthropics/claude-code).

##

​

Why Claude Code?

Claude Code operates directly in your terminal, understanding your project
context and taking real actions. No need to manually add files to context -
Claude will explore your codebase as needed. Claude Code uses
`claude-3-7-sonnet-20250219` by default.

###

​

Enterprise integration

Claude Code seamlessly integrates with enterprise AI platforms. You can
connect to [Amazon Bedrock or Google Vertex AI](/en/docs/claude-code/bedrock-
vertex) for secure, compliant deployments that meet your organization’s
requirements.

###

​

Security and privacy by design

Your code’s security is paramount. Claude Code’s architecture ensures:

  * **Direct API connection** : Your queries go straight to Anthropic’s API without intermediate servers
  * **Works where you work** : Operates directly in your terminal
  * **Understands context** : Maintains awareness of your entire project structure
  * **Takes action** : Performs real operations like editing files and creating commits

##

​

Getting started

To get started with Claude Code, follow our [installation
guide](/en/docs/claude-code/getting-started) which covers system requirements,
installation steps, and authentication process.

##

​

Quick tour

Here’s what you can accomplish with Claude Code:

###

​

From questions to solutions in seconds

    
    
    # Ask questions about your codebase
    claude
    > how does our authentication system work?
    
    # Create a commit with one command
    claude commit
    
    # Fix issues across multiple files
    claude "fix the type errors in the auth module"
    

###

​

Understand unfamiliar code

    
    
    > what does the payment processing system do?
    > find where user permissions are checked
    > explain how the caching layer works
    

###

​

Automate Git operations

    
    
    > commit my changes
    > create a pr
    > which commit added tests for markdown back in December?
    > rebase on main and resolve any merge conflicts
    

##

​

Next steps

## [Getting startedInstall Claude Code and get up and
running](/en/docs/claude-code/getting-started)## [Core featuresExplore what
Claude Code can do for you](/en/docs/claude-code/common-tasks)##
[CommandsLearn about CLI commands and controls](/en/docs/claude-
code/commands)## [ConfigurationCustomize Claude Code for your
workflow](/en/docs/claude-code/configuration)

##

​

Additional resources

## [Claude Code tutorialsStep-by-step guides for common
tasks](/en/docs/claude-code/tutorials)## [TroubleshootingSolutions for common
issues with Claude Code](/en/docs/claude-code/troubleshooting)## [Bedrock &
Vertex integrationsConfigure Claude Code with Amazon Bedrock or Google Vertex
AI](/en/docs/claude-code/bedrock-vertex)## [Reference implementationClone our
development container reference
implementation.](https://github.com/anthropics/claude-
code/tree/main/.devcontainer)

##

​

License and data usage

Claude Code is provided as a Beta research preview under Anthropic’s
[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-
terms).

###

​

How we use your data

We aim to be fully transparent about how we use your data. We may use feedback
to improve our products and services, but we will not train generative models
using your feedback from Claude Code. Given their potentially sensitive
nature, we store user feedback transcripts for only 30 days.

####

​

Feedback transcripts

If you choose to send us feedback about Claude Code, such as transcripts of
your usage, Anthropic may use that feedback to debug related issues and
improve Claude Code’s functionality (e.g., to reduce the risk of similar bugs
occurring in the future). We will not train generative models using this
feedback.

###

​

Privacy safeguards

We have implemented several safeguards to protect your data, including limited
retention periods for sensitive information, restricted access to user session
data, and clear policies against using feedback for model training.

For full details, please review our [Commercial Terms of
Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy
Policy](https://www.anthropic.com/legal/privacy).

###

​

License

© Anthropic PBC. All rights reserved. Use is subject to Anthropic’s
[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-
terms).

Was this page helpful?

YesNo

[Getting started](/en/docs/claude-code/getting-started)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

