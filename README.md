# Alfred Workflows

### Setup a new workflow project

1. Create workflow in Alfred
    - Use a `Run Script` action
    - Use `/bin/bash` as the language
    - Use `{query}` as input
    - The script value should be whatever language parser that workflow is based with `{query}` at the end of the command
        - Example: `python main.py {query}`
    - Use `Spaces` as the escaping mechanism

2. Copy the contents of the workflow folder created by Alfred and put it in the workflow project directory
    - This is typically a `info.plist` and a logo file referenced within _info.plist_

3. Take note of the directory path created by Alfred of the workflow

4. Remove the generated workflow directory

5. Symlink the workflow project directory, use the path from step 3 

### Using a workflow project

Use the same steps with `Setup a new workflow project` but just skipping step 2
