# LLDB Scripts

In your `~/.lldbinit` file add the following command:

`command script import /path/to/LLDBScripts/lldbinit.py`

## Available commands

### jq
The jq command works exactly like jq on the command line. On the lldb prompt, use the following command: `jq 'options' variableToInspect`

The variable to inspect must be an instance of a Swift unwrapped string, NSString (with the `-n` option), or an NSData object. 

The options you can give to the command are:

- `-c` for compact output. By default jq will output pretty-printed JSON
- `-n` to support `NSString` instances

You can find more information about jq here: https://stedolan.github.io/jq/

Many thanks to Aijaz Ansari for most of the jq loading work: https://github.com/aijaz/lldbPythonScripts
