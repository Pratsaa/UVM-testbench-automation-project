# UVM Testbench Automation - README

## Overview
This tool automates the generation of UVM testbench components using Python scripts. It is designed to help users quickly set up UVM environments by parsing interface definitions and generating the required SystemVerilog files. The tool is designed to automatically generate a UVM script that is immediately compilable (with very minimal input for users beside inputting the relative path in some cases). This tool is solely meant to be used on the Linux terminal, and all subseqeunt commands are written as per Linux conventions. The initial versions of this tool were created by Pratyush Ashok Anand, primarily to aid the verification applications of Auradine Inc./Upscale AI. 

## Getting Started

### 1. Prepare Your Interface Definitions
- Place your interface definitions (with all required signals and parameters) in the `template_sigs.sv` file.
- Each interface should be clearly defined and include all necessary ports and parameters.

### 2. Run the Automation Script
- The main script is `uvmgen_cli.py` located in the `UVM_tb_automation` folder.
- To generate UVM components, do to the `UVM_tb_automation` run:
  python3 uvmgen_cli.py -m <`insert name of your UVM FOLDER`> -o <`insert the output directory for your file`> --design template_sigs.sv --interface
  eg: python3 uvmgen_cli.py -m finaltest1 -o ../common_ip_17june/verif/ --design template_sigs.sv --interface
- NOTE: --interface is just a flag. Just including it sets its value to True. You don't provide any value after it.
- The script will parse `template_sigs.sv` and generate UVM files in the appropriate locations.

### 3. Output Files
- Generated files include UVM agents, drivers, monitors, sequences, and environment files.
- Output files are placed in the `templates_uvm` folder and other relevant subfolders.
- The following template files are provided in the `templates_uvm` folder and are used by the automation scripts (`uvmgen_cli.py`, parser files):

  - `template_sigs.sv`           # Main input file for interface definitions
  - `uvm_agent.sv`               # UVM agent template (SystemVerilog)
  - `uvm_agent_pkg.sv`           # UVM agent package template
  - `uvm_driver.sv`              # UVM driver template
  <!-- - `uvm_driver.py`              # Python template for UVM driver generation (NOT USED) -->
  - `uvm_monitor.sv`             # UVM monitor template
  <!-- - `uvm_monitor.py`             # Python template for UVM monitor generation (NOT USED) -->
  - `uvm_scoreboard.py`          # Python template for UVM scoreboard generation
  - `uvm_env.py`                 # Python template for UVM environment generation
  - `uvm_harness.py`             # Python template for harness generation
  - `uvm_interface.py`           # Python template for interface generation
  - `uvm_seq_item.sv`            # UVM sequence item template
  - `uvm_tb_pkg.py`              # Python template for testbench package
  - `uvm_tb_top.py`              # Python template for top-level testbench
  - `uvm_test.py`                # Python template for UVM test generation
  - `uvm_basic_seq.py`           # Python template for basic sequence generation
  - `Makefile_template.py`       # Python template for Makefile generation
  - `designF_template.py`        # Python template for design.F file generation
  - `verifF_template.py`         # Python template for verif.F file generation

- These templates are automatically used and populated by the automation scripts to generate the required UVM testbench files. You can customize these templates as needed to fit your project requirements.

### 4. Modifications that the user has to make *after* generating the TB
- Make sure that the expected file structure of the UVM testbench is correct
- Make sure that the path to the Makefile is also correct (found at the very end of Makefile file)
- Make sure that the path to the design file is correctly entered at the end of the design.F file
- Make sure that all the verif.F paths line up properly

### 5. Running the UVM tb on VCS
- The command to compile and run the tb is as follows: `runsim.sh -b build -t <insert the name of test file> -r "+sim_test_seq_name=<insert name of generated basic seqeunce file>" o <insert the name of the output directory of your choice>`
- Eg: runsim.sh -b build -t finaltest1_test -r "+sim_test_seq_name=finaltest1_basic_seq" -o design_file_1
- Try running and compiling the UVM testbench, if it fails the most likely error is that certain sub-files have not been included in the design.F file
- Upon resolving the errors (which will most likely be design.F related or spelling mistakes), the UVM tb should compile but naturally test will fail

## File Structure of the script
- `UVM_tb_automation/`
  - `uvmgen_cli.py`: Main automation script
  - `multi_interface_parser.py`: Helper script for parsing multiple interfaces
  - `signal_parser/`: Contains signal extraction utilities
  - `templates_uvm/`: Contains templates and generated UVM files
    - `template_sigs.sv`: Input file for interface definitions
    - miscelaneous template files for key components/objects

## *Expected* File Structure of the generated UVM testbench

After running the automation script, your UVM testbench directory will be organized into three main folders:

```
<output_directory>/
├── sim/
│   ├── Makefile                # Compilation and simulation script
│   ├── build/                  # Build artifacts and compiled files, will only appear after script is run for the first time 
│   ├── <name of folder>_test/           # Simulation outputs and logs, will only appear after script is run for the first time 
│   └── runsim.history          # History of simulation runs, will only appear after script is run for the first time 
│
├── tb/
│   ├── tb_top.sv               # Top-level testbench module
│   ├── tb_pkg.sv               # Testbench package
│   ├── <name of folder>_env.sv          # UVM environment file
│   ├── <name of folder>_harness.sv      # Additional harness file
│   ├── <name of folder>_scoreboard.sv   # Scoreboard for checking results
│   ├── design.F                # Design file list
│   ├── verif.F                 # Verification file list
│   ├── Agent1/              # First agent files (pkg, if, driver, monitor, etc.)
│   ├── Agent2/            # Second agent files (if applicable)
│   └── ...                     # Other agent or utility folders/files
│
├── tests/
│   ├── <name of folder>_basic_seq.sv    # Basic sequence file
│   └── <name of folder>_test.sv         # UVM test file
│   └── ...                     # Additional test or sequence files
```

**Notes:**
- The `sim/` folder contains all simulation-related scripts, outputs, and build artifacts.
- The `tb/` folder contains the main testbench files, agent directories, environment, harness, scoreboard, and configuration files.
- The `tests/` folder contains UVM test and sequence files.
- Make sure to update the paths in `Makefile`, `design.F`, and `verif.F` as needed after generation.
- Additional files and folders may be generated depending on your input and options.

This structure matches the conventions used in the `newtest` testbench and ensures clarity and modularity for users working with the generated UVM testbench.


## Tips for First-Time Users
- Ensure your interface definitions in `template_sigs.sv` are correct and complete.
- Review the generated files for customization as needed.
- If you encounter errors, check the format of your input file and refer to comments in the scripts for guidance.

### Future Improvements
- The incorporation of the clock generator module as well as the PWM scoreboard components
- Additional logic to offer better support for subscribers such as predictors, advanced scoreboard and so on 
- Backtracking to trace the exact path of different verif.F and design.F
- Use of more efficient agent config methods


## Support
- For questions or issues, please contact the script author or refer to comments in the Python files for troubleshooting tips.
- Contact details: `Pratyush Ashok Anand`, email: `pratyushashokanand@gmail.com`
