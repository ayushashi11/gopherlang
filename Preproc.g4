lexer grammar Preproc;
PREPROC_START:'$#' -> pushMode(Pre_proc);
mode Pre_proc;
    PREPROC_END:'#$' -> popMode;
