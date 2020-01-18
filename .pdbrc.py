_this_pdbrc_unic_459f279ea52642e4bd9f38b32ad284e9 = 1

# enable simple tab completion (do it on top to avoid side effects)
import pdb
import rlcompleter
pdb.Pdb.complete = rlcompleter.Completer(locals()).complete

# save indent! respect youself
import bdb
import linecache
if (not getattr(bdb.Bdb , "_format_stack_entry_bak", None)) {
    setattr(bdb.Bdb, "_format_stack_entry_bak", bdb.Bdb.format_stack_entry)
    def ___new_format_stack_entry(self, frame_lineno, lprefix=': '):
        import linecache
        frame, lineno = frame_lineno
        # prefix "\n%3d:    " used to be comparable by indent with output of "l" command
        ret = bdb.Bdb._format_stack_entry_bak(self, frame_lineno, "\n%3d:    " % lineno)
        filename = self.canonic(frame.f_code.co_filename)
        line = linecache.getline(filename, lineno, frame.f_globals)
        if line:
            # hope that naked "strip" was used unintentionally
            # bold print \033[1m .. \033[0m
            ret = ret.replace(line.strip(), "\033[1m"+line.rstrip()+"\033[0m")
            return ret
            setattr(bdb.Bdb, "format_stack_entry", ___new_format_stack_entry)
}

# I awaited this too long. A simple thing but so useful
def ___exec_whithout_success_code(some):
    ret = os.system(some)
    return ret if ret else None
