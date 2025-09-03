def generate_env_file(env_name, interface_list):
    env_class = env_name.lower()
    env_macro = env_name.upper()

    # Agent declarations
    agent_decls = "\n".join([f"  {iface}_agent m_{iface}_agent;" for iface in interface_list])
    agent_creates = "\n".join([f"    m_{iface}_agent = {iface}_agent::type_id::create(\"m_{iface}_agent\", this);" for iface in interface_list])

    # Scoreboard declaration
    scoreboard_decl = f" // {env_class}_scoreboard m_scoreboard;"

    # Interface fetch (optional if not needed at env level)
    # Can be added here if you want to fetch interfaces via `uvm_config_db`

    # Connect monitor AP to scoreboard export
    connect_lines = "\n".join([
        f"    //m_{iface}_agent.m_monitor.ap.connect(m_scoreboard.{iface}_export);"
        for iface in interface_list
    ])

    return f"""\
`ifndef {env_macro}_ENV_SV
`define {env_macro}_ENV_SV

class {env_class}_env extends uvm_env;
  `uvm_component_utils({env_class}_env)

{agent_decls}
{scoreboard_decl}

  function new(string name = "{env_class}_env", uvm_component parent = null);
    super.new(name, parent);
  endfunction

  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
{agent_creates}
    //m_scoreboard = {env_class}_scoreboard::type_id::create("m_scoreboard", this);
  endfunction

  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
{connect_lines}
  endfunction

endclass

`endif
"""
