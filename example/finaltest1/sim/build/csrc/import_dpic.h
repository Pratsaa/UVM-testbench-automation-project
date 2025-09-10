
 extern int vc_uvmOnewayHash(/* INPUT */const char* string_in, /* INPUT */int seed);

 extern int vc_uvmCreateRandomSeed(/* INPUT */const char* string_in, /* INPUT */int seed);

 extern void vc_uvmReseed();

 extern int uvm_hdl_check_path(/* INPUT */const char* path);

 extern int uvm_hdl_deposit(/* INPUT */const char* path, const /* INPUT */svLogicVecVal *value);

 extern int uvm_hdl_force(/* INPUT */const char* path, const /* INPUT */svLogicVecVal *value);

 extern int uvm_hdl_release_and_read(/* INPUT */const char* path, /* INOUT */svLogicVecVal *value);

 extern int uvm_hdl_release(/* INPUT */const char* path);

 extern int uvm_hdl_read(/* INPUT */const char* path, /* OUTPUT */svLogicVecVal *value);

 extern SV_STRING uvm_hdl_read_string(/* INPUT */const char* path);

 extern int uvm_memory_load(/* INPUT */const char* nid, /* INPUT */const char* scope, /* INPUT */const char* fileName, /* INPUT */const char* radix, /* INPUT */const char* startaddr, /* INPUT */const char* endaddr, /* INPUT */const char* types);

 extern SV_STRING uvm_dpi_get_next_arg_c(/* INPUT */int init);

 extern SV_STRING uvm_dpi_get_tool_name_c();

 extern SV_STRING uvm_dpi_get_tool_version_c();

 extern void* uvm_dpi_regcomp(/* INPUT */const char* regex);

 extern int uvm_dpi_regexec(/* INPUT */void* preg, /* INPUT */const char* str);

 extern void uvm_dpi_regfree(/* INPUT */void* preg);

 extern int uvm_re_match(/* INPUT */const char* re, /* INPUT */const char* str);

 extern SV_STRING uvm_glob_to_re(/* INPUT */const char* glob);

 extern void fsdbTransDPI_scope_add_logicvec_attribute(/* OUTPUT */int *state, /* INPUT */const char* scope_fullname, /* INPUT */const char* attribute_name, const /* INPUT */svLogicVecVal *attribute, /* INPUT */int numbit, /* INPUT */const char* options);

 extern void fsdbTransDPI_scope_add_int_attribute(/* OUTPUT */int *state, /* INPUT */const char* scope_fullname, /* INPUT */const char* attribute_name, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_scope_add_string_attribute(/* OUTPUT */int *state, /* INPUT */const char* scope_fullname, /* INPUT */const char* attribute_name, /* INPUT */const char* attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_scope_add_real_attribute(/* OUTPUT */int *state, /* INPUT */const char* scope_fullname, /* INPUT */const char* attribute_name, /* INPUT */double attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_scope_add_enum_int_attribute(/* OUTPUT */int *state, /* INPUT */const char* scope_fullname, /* INPUT */const char* attribute_name, /* INPUT */unsigned int enum_id, /* INPUT */int attribute, /* INPUT */const char* options);

 extern int fsdbTransDPI_create_stream_begin(/* OUTPUT */int *state, /* INPUT */const char* stream_fullname, /* INPUT */const char* description, /* INPUT */const char* options);

 extern void fsdbTransDPI_define_logicvec_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, const /* INPUT */svLogicVecVal *attribute, /* INPUT */int numbit, /* INPUT */const char* options);

 extern void fsdbTransDPI_define_int_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_define_string_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */const char* attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_define_real_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */double attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_define_enum_int_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */unsigned int enum_id, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_stream_add_logicvec_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, const /* INPUT */svLogicVecVal *attribute, /* INPUT */int numbit, /* INPUT */const char* options);

 extern void fsdbTransDPI_stream_add_int_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_stream_add_string_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */const char* attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_stream_add_real_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */double attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_stream_add_enum_int_attribute(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* attribute_name, /* INPUT */unsigned int enum_id, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_create_stream_end(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* options);

 extern long long fsdbTransDPI_begin(/* OUTPUT */int *state, /* INPUT */int sid, /* INPUT */const char* trans_type, /* INPUT */const char* options);

 extern void fsdbTransDPI_set_label(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* label, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_tag(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* tag, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_logicvec_attribute(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, const /* INPUT */svLogicVecVal *attribute, /* INPUT */int numbit, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_int_attribute(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_string_attribute(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */const char* attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_real_attribute(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */double attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_enum_int_attribute(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */unsigned int enum_id, /* INPUT */int attribute, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_logicvec_attribute_with_expected_value(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, const /* INPUT */svLogicVecVal *attribute, /* INPUT */int numbit, const /* INPUT */svLogicVecVal *expected_val, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_int_attribute_with_expected_value(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */int attribute, /* INPUT */int expected_val, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_string_attribute_with_expected_value(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */const char* attribute, /* INPUT */const char* expected_val, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_real_attribute_with_expected_value(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */double attribute, /* INPUT */double expected_val, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_enum_int_attribute_with_expected_value(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* attribute_name, /* INPUT */unsigned int enum_id, /* INPUT */int attribute, /* INPUT */int expected_val, /* INPUT */const char* options);

 extern void fsdbTransDPI_end(/* OUTPUT */int *state, /* INPUT */long long tid, /* INPUT */const char* options);

 extern void fsdbTransDPI_add_relation(/* OUTPUT */int *state, /* INPUT */const char* rel_name, /* INPUT */long long master_tid, /* INPUT */long long slave_tid, /* INPUT */const char* options);

 extern unsigned int fsdbTransDPI_get_enum_id(/* OUTPUT */int *state, /* INPUT */const char* enum_var_name);

 extern SV_STRING fsdbTransDPI_get_class_str(/* OUTPUT */int *state, /* INPUT */const char* class_var_name, /* INPUT */const char* options);
