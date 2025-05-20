# CLI usage

Claude Code

# CLI usage and controls

Learn how to use Claude Code from the command line, including CLI commands,
flags, and slash commands.

##

​

Getting started

Claude Code provides two main ways to interact:

  * **Interactive mode** : Run `claude` to start a REPL session
  * **One-shot mode** : Use `claude -p "query"` for quick commands

    
    
    # Start interactive mode
    claude
    
    # Start with an initial query
    claude "explain this project"
    
    # Run a single command and exit
    claude -p "what does this function do?"
    
    # Process piped content
    cat logs.txt | claude -p "analyze these errors"
    

##

​

CLI commands

Command| Description| Example  
---|---|---  
`claude`| Start interactive REPL| `claude`  
`claude "query"`| Start REPL with initial prompt| `claude "explain this
project"`  
`claude -p "query"`| Run one-off query, then exit| `claude -p "explain this
function"`  
`cat file | claude -p "query"`| Process piped content| `cat logs.txt | claude -p "explain"`  
`claude -c`| Continue most recent conversation| `claude -c`  
`claude -c -p "query"`| Continue in print mode| `claude -c -p "Check for type
errors"`  
`claude -r "<session-id>" "query"`| Resume session by ID| `claude -r "abc123"
"Finish this PR"`  
`claude config`| Configure settings| `claude config set --global theme dark`  
`claude update`| Update to latest version| `claude update`  
`claude mcp`| Configure Model Context Protocol servers| [See MCP section in
tutorials](/en/docs/claude-code/tutorials#set-up-model-context-protocol-mcp)  
  
##

​

CLI flags

Customize Claude Code’s behavior with these command-line flags:

Flag| Description| Example  
---|---|---  
`--print`, `-p`| Print response without interactive mode (see [detailed print
mode documentation](/_sites/docs.anthropic.com/en/docs/claude-code/cli-
usage#print-mode-details) below)| `claude -p "query"`  
`--output-format`| Specify output format for print mode (options: `text`,
`json`, `stream-json`)| `claude -p "query" --output-format json`  
`--verbose`| Enable verbose logging, shows full turn-by-turn output (helpful
for debugging in both print and interactive modes)| `claude --verbose`  
`--max-turns`| Limit the number of agentic turns in non-interactive mode|
`claude -p --max-turns 3 "query"`  
`--permission-prompt-tool`| Specify an MCP tool to handle permission prompts
in non-interactive mode| `claude -p --permission-prompt-tool mcp_auth_tool
"query"`  
`--resume`| Resume a specific session by ID, or by choosing in interactive
mode| `claude --resume abc123 "query"`  
`--continue`| Load the most recent conversation in the current directory|
`claude --continue`  
`--dangerously-skip-permissions`| Skip permission prompts (use with caution)|
`claude --dangerously-skip-permissions`  
  
The `--output-format json` flag is particularly useful for scripting and
automation, allowing you to parse Claude’s responses programmatically.

###

​

Print mode details

The `-p` (or `--print`) flag enables non-interactive mode in Claude Code,
allowing you to pipe input and output for programmatic use. This flag supports
various output formats for different use cases.

####

​

Basic usage

    
    
    # Basic print mode - outputs just the final response text
    claude -p "Explain how to use the print flag"
    
    # With stdin input
    echo "What is 2+2?" | claude -p
    
    # Resume a session in print mode with a prompt
    claude -p --resume <session-id> "Resume session with this prompt"
    

####

​

Output formats

The `--output-format` option (used with `-p`) supports three formats:

##### 1\. Text Output (default)

    
    
    claude -p "Explain the output formats"
    # Outputs just the response text
    

##### 2\. JSON Output

    
    
    claude -p --output-format json "Explain how to use JSON output"
    

Outputs a structured JSON object:

    
    
    {
      "cost_usd": 0.003,
      "duration_ms": 1234,
      "duration_api_ms": 800,
      "result": "The response text here...",
      "session_id": "abc123"
    }
    

##### 3\. Streaming JSON Output

    
    
    claude -p --output-format stream-json "Create a Python script"
    

In streaming mode, each message is output as a separate JSON object as it’s
received:

  * Tool use messages
  * Assistant text messages
  * Tool result messages
  * Final system message with stats

####

​

Verbose output with print mode

When using `--verbose` with `-p`, it must be paired with `--output-format
json` or `--output-format stream-json`:

    
    
    claude -p --verbose --output-format json "Debug this code"
    

In verbose JSON mode, the output includes the full conversation transcript:

    
    
    [
      {
        "role": "user",
        "content": "Debug this code"
      },
      {
        "role": "assistant",
        "content": "I'll help you debug that code..."
      },
      {
        "role": "system",
        "cost_usd": 0.003,
        "duration_ms": 1234,
        "duration_api_ms": 800,
        "result": "The response text here...",
        "session_id": "abc123"
      }
    ]
    

####

​

Additional options for print mode

##### Max Turns

    
    
    claude -p --max-turns 3 "Fix this code" < file.py
    

Limits the number of agentic turns in non-interactive mode.

##### Permission Prompt Tool

    
    
    claude -p --permission-prompt-tool mcp_auth_tool "Create a file"
    

Specifies an MCP tool to handle permission prompts in non-interactive mode.

##### Resume Session

    
    
    claude -p --resume abc123 "Resume session with this prompt"
    

Resume a specific session by ID in print mode with a new prompt.

####

​

Continue Session

    
    
    claude -c -p "Continue with this next task"
    

Continue the last conversation in this project.

##

​

Slash commands

Control Claude’s behavior during an interactive session:

Command| Purpose  
---|---  
`/bug`| Report bugs (sends conversation to Anthropic)  
`/clear`| Clear conversation history  
`/compact [instructions]`| Compact conversation with optional focus
instructions  
`/config`| View/modify configuration  
`/cost`| Show token usage statistics  
`/doctor`| Checks the health of your Claude Code installation  
`/help`| Get usage help  
`/init`| Initialize project with CLAUDE.md guide  
`/login`| Switch Anthropic accounts  
`/logout`| Sign out from your Anthropic account  
`/memory`| Edit CLAUDE.md memory files  
`/pr_comments`| View pull request comments  
`/review`| Request code review  
`/status`| View account and system statuses  
`/terminal-setup`| Install Shift+Enter key binding for newlines (iTerm2 and
VSCode only)  
`/vim`| Enter vim mode for alternating insert and command modes  
  
##

​

Special shortcuts

###

​

Quick memory with `#`

Add memories instantly by starting your input with `#`:

    
    
    # Always use descriptive variable names
    

You’ll be prompted to select which memory file to store this in.

###

​

Line breaks in terminal

Enter multiline commands using:

  * **Quick escape** : Type `\` followed by Enter
  * **Keyboard shortcut** : Option+Enter (or Shift+Enter if configured)

To set up Option+Enter in your terminal:

**For Mac Terminal.app:**

  1. Open Settings → Profiles → Keyboard
  2. Check “Use Option as Meta Key”

**For iTerm2 and VSCode terminal:**

  1. Open Settings → Profiles → Keys
  2. Under General, set Left/Right Option key to “Esc+”

**Tip for iTerm2 and VSCode users** : Run `/terminal-setup` within Claude Code
to automatically configure Shift+Enter as a more intuitive alternative.

See [terminal setup in settings](/en/docs/claude-code/settings#line-breaks)
for configuration details.

##

​

Vim Mode

Claude Code supports a subset of Vim keybindings that can be enabled with
`/vim` or configured via `/config`.

The supported subset includes:

  * Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
  * Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
  * Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)

Was this page helpful?

YesNo

[Common tasks](/en/docs/claude-code/common-tasks)[Memory
management](/en/docs/claude-code/memory)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

