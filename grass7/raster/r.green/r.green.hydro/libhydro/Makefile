MODULE_TOPDIR = ../../../..

include $(MODULE_TOPDIR)/include/Make/Other.make
include $(MODULE_TOPDIR)/include/Make/Python.make

MODULES = basin plant optimal __init__

PGM = r.green
LIBDIR = libhydro
ETCDIR = $(ETC)/$(PGM)/$(LIBDIR)

PYFILES := $(patsubst %,$(ETCDIR)/%.py,$(MODULES))
PYCFILES := $(patsubst %,$(ETCDIR)/%.pyc,$(MODULES))

default: $(PYFILES) $(PYCFILES)

$(ETCDIR):
	$(MKDIR) $@

$(ETCDIR)/%: % | $(ETCDIR)
	$(INSTALL_DATA) $< $@

install:
	$(MKDIR) $(INST_DIR)/etc/$(PGM)
	cp -r $(ETCDIR) $(INST_DIR)/etc/$(PGM)/$(LIBDIR)
