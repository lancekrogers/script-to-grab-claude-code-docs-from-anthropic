# Settings

Claude Code

# Claude Code settings

Learn how to configure Claude Code with global and project-level settings,
themes, and environment variables.

Claude Code offers a variety of settings to configure its behavior to meet
your needs. You can configure Claude Code by running `claude config` in your
terminal, or the `/config` command when using the interactive REPL.

##

​

Configuration hierarchy

The new `settings.json` file is our official mechanism for configuring Claude
Code through hierarchical settings.

User settings are defined in `~/.claude/settings.json` and apply to all
projects.

Project settings are saved in your project directory under
`.claude/settings.json` for shared settings, and `.claude/settings.local.json`
for local project settings. Claude Code will configure git to ignore
`.claude/settings.local.json` when it is created.

For enterprise deployments of Claude Code, we also support enterprise managed
policy settings. These take precedence over user and project settings. System
administrators can deploy policies to `/Library/Application
Support/ClaudeCode/policies.json` on macOS and `/etc/claude-
code/policies.json` on Linux and Windows via WSL.

Example settings.json

    
    
    {
      "permissions": {
        "allow": [
          "Bash(npm run lint)",
          "Bash(npm run test:*)",
          "Read(~/.zshrc)"
        ],
        "deny": [
          "Bash(curl:*)"
        ]
      },
      "env": {
        "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
        "OTEL_METRICS_EXPORTER": "otlp"
      }
    }
    

###

​

Settings precedence

Settings are applied in order of precedence, with later sources overriding
previous sources:

  * User settings
  * Shared project settings
  * Local project settings
  * Command line arguments
  * Enterprise policies

##

​

Configuration options

Claude Code supports global and project-level configuration.

To manage your configurations, use the following commands:

  * List settings: `claude config list`
  * See a setting: `claude config get <key>`
  * Change a setting: `claude config set <key> <value>`
  * Push to a setting (for lists): `claude config add <key> <value>`
  * Remove from a setting (for lists): `claude config remove <key> <value>`

By default `config` changes your project configuration. To manage your global
configuration, use the `--global` (or `-g`) flag.

###

​

Global configuration

To set a global configuration, use `claude config set -g <key> <value>`:

Key| Value| Description  
---|---|---  
`autoUpdaterStatus`| `disabled` or `enabled`| Enable or disable the auto-
updater (default: `enabled`)  
`env`| JSON (eg. `'{"FOO": "bar"}'`)| Environment variables that will be
applied to every session  
`preferredNotifChannel`| `iterm2`, `iterm2_with_bell`, `terminal_bell`, or
`notifications_disabled`| Where you want to receive notifications (default:
`iterm2`)  
`theme`| `dark`, `light`, `light-daltonized`, or `dark-daltonized`| Color
theme  
`verbose`| `true` or `false`| Whether to show full bash and command outputs
(default: `false`)  
  
###

​

Project configuration

Manage project configuration with `claude config set <key> <value>` (without
the `-g` flag):

Key| Value| Description  
---|---|---  
`allowedTools`| array of tools| Which tools can run without manual approval  
`ignorePatterns`| array of glob strings| Which files/directories are ignored
when using tools  
  
For example:

    
    
    # Let npm test to run without approval
    claude config add allowedTools "Bash(npm test)"
    
    # Let npm test and any of its sub-commands to run without approval
    claude config add allowedTools "Bash(npm test:*)"
    
    # Instruct Claude to ignore node_modules
    claude config add ignorePatterns node_modules
    claude config add ignorePatterns "node_modules/**"
    

##

​

Permissions

You can manage Claude Code’s tool permissions with `/allowed-tools`. This UI
lists all permission rules and the settings.json file they are sourced from.

  * **Allow** rules will allow Claude Code to use the specified tool without further manual approval.
  * **Deny** rules will prevent Claude Code from using the specified tool. Deny rules take precedence over allow rules.

Permission rules use the format: `Tool(optional-specifier)`.

For example, adding `WebFetch` to the list of allow rules would allow any use
of the web fetch tool without requiring user approval. See the list of [tools
available to Claude](/en/docs/claude-code/security#tools-available-to-claude)
(use the name in parentheses when provided.)

Some tools use the optional specifier for more fine-grained permission
controls. For example, an allow rule with `WebFetch(domain:example.com)` would
allow fetches to example.com but not other URLs.

Bash rules can be exact matches like `Bash(npm run build)`, or prefix matches
when they end with `:*` like `Bash(npm run test:*)`

`Read()` and `Edit()` rules follow the [gitignore](https://git-
scm.com/docs/gitignore) specification. Patterns are resolved relative to the
directory containing `.claude/settings.json`. To reference an absolute path,
use `//`. For a path relative to your home directory, use `~/`. For example
`Read(//tmp/build_cache)` or `Edit(~/.zshrc)`. Claude will also make a best-
effort attempt to apply Read and Edit rules to other file-related tools like
Grep, Glob, and LS.

MCP tool names follow the format: `mcp__server_name__tool_name` where:

  * `server_name` is the name of the MCP server as configured in Claude Code
  * `tool_name` is the specific tool provided by that server

More examples:

Rule| Description  
---|---  
`Bash(npm run build)`| Matches the exact Bash command `npm run build`.  
`Bash(npm run test:*)`| Matches Bash commands starting with `npm run test`.
See note below about command separator handling.  
`Edit(~/.zshrc)`| Matches the `~/.zshrc` file.  
`Read(node_modules/**)`| Matches any `node_modules` directory.  
`mcp__puppeteer__puppeteer_navigate`| Matches the `puppeteer_navigate` tool
from the `puppeteer` MCP server.  
`WebFetch(domain:example.com)`| Matches fetch requests to example.com  
  
Claude Code is aware of command separators (like `&&`) so a prefix match rule
like `Bash(safe-cmd:*)` won’t give it permission to run the command `safe-cmd
&& other-cmd`

##

​

Auto-updater permission options

When Claude Code detects that it doesn’t have sufficient permissions to write
to your global npm prefix directory (required for automatic updates), you’ll
see a warning that points to this documentation page. For detailed solutions
to auto-updater issues, see the [troubleshooting guide](/en/docs/claude-
code/troubleshooting#auto-updater-issues).

###

​

Recommended: Create a new user-writable npm prefix

    
    
    # First, save a list of your existing global packages for later migration
    npm list -g --depth=0 > ~/npm-global-packages.txt
    
    # Create a directory for your global packages
    mkdir -p ~/.npm-global
    
    # Configure npm to use the new directory path
    npm config set prefix ~/.npm-global
    
    # Note: Replace ~/.bashrc with ~/.zshrc, ~/.profile, or other appropriate file for your shell
    echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
    
    # Apply the new PATH setting
    source ~/.bashrc
    
    # Now reinstall Claude Code in the new location
    npm install -g @anthropic-ai/claude-code
    
    # Optional: Reinstall your previous global packages in the new location
    # Look at ~/npm-global-packages.txt and install packages you want to keep
    # npm install -g package1 package2 package3...
    

**Why we recommend this option:**

  * Avoids modifying system directory permissions
  * Creates a clean, dedicated location for your global npm packages
  * Follows security best practices

Since Claude Code is actively developing, we recommend setting up auto-updates
using the recommended option above.

###

​

Disabling the auto-updater

If you prefer to disable the auto-updater instead of fixing permissions, you
can use:

    
    
    claude config set -g autoUpdaterStatus disabled
    

##

​

Optimize your terminal setup

Claude Code works best when your terminal is properly configured. Follow these
guidelines to optimize your experience.

**Supported shells** :

  * Bash
  * Zsh
  * Fish

###

​

Themes and appearance

Claude cannot control the theme of your terminal. That’s handled by your
terminal application. You can match Claude Code’s theme to your terminal
during onboarding or any time via the `/config` command

###

​

Line breaks

You have several options for entering linebreaks into Claude Code:

  * **Quick escape** : Type `\` followed by Enter to create a newline
  * **Keyboard shortcut** : Press Option+Enter (Meta+Enter) with proper configuration

To set up Option+Enter in your terminal:

**For Mac Terminal.app:**

  1. Open Settings → Profiles → Keyboard
  2. Check “Use Option as Meta Key”

**For iTerm2 and VSCode terminal:**

  1. Open Settings → Profiles → Keys
  2. Under General, set Left/Right Option key to “Esc+”

**Tip for iTerm2 and VSCode users** : Run `/terminal-setup` within Claude Code
to automatically configure Shift+Enter as a more intuitive alternative.

###

​

Notification setup

Never miss when Claude completes a task with proper notification
configuration:

####

​

Terminal bell notifications

Enable sound alerts when tasks complete:

    
    
    claude config set --global preferredNotifChannel terminal_bell
    

**For macOS users** : Don’t forget to enable notification permissions in
System Settings → Notifications → [Your Terminal App].

####

​

iTerm 2 system notifications

For iTerm 2 alerts when tasks complete:

  1. Open iTerm 2 Preferences
  2. Navigate to Profiles → Terminal
  3. Enable “Silence bell” and “Send notification when idle”
  4. Set your preferred notification delay

Note that these notifications are specific to iTerm 2 and not available in the
default macOS Terminal.

###

​

Handling large inputs

When working with extensive code or long instructions:

  * **Avoid direct pasting** : Claude Code may struggle with very long pasted content
  * **Use file-based workflows** : Write content to a file and ask Claude to read it
  * **Be aware of VS Code limitations** : The VS Code terminal is particularly prone to truncating long pastes

###

​

Vim Mode

Claude Code supports a subset of Vim keybindings that can be enabled with
`/vim` or configured via `/config`.

The supported subset includes:

  * Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
  * Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`
  * Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)

##

​

Environment variables

Claude Code supports the following environment variables to control its
behavior:

Variable| Purpose  
---|---  
`DISABLE_AUTOUPDATER`| Set to `1` to disable the automatic updater  
`DISABLE_BUG_COMMAND`| Set to `1` to disable the `/bug` command  
`DISABLE_COST_WARNINGS`| Set to `1` to disable cost warning messages  
`DISABLE_ERROR_REPORTING`| Set to `1` to opt out of Sentry error reporting  
`DISABLE_TELEMETRY`| Set to `1` to opt out of Statsig telemetry (note that
Statsig events do not include user data like code, file paths, or bash
commands)  
`HTTP_PROXY`| Specify HTTP proxy server for network connections  
`HTTPS_PROXY`| Specify HTTPS proxy server for network connections  
`MCP_TIMEOUT`| Timeout in milliseconds for MCP server startup  
`MCP_TOOL_TIMEOUT`| Timeout in milliseconds for MCP tool execution  
  
Was this page helpful?

YesNo

[Memory management](/en/docs/claude-code/memory)[Security](/en/docs/claude-
code/security)

[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)

