#!/usr/bin/env python

from string import maketrans # used to create translation table

# create a mapping table from strings. Table maps char on in, to char on out

in_table = "abcdefghijklmnopqrstuvwxyz"
out_table = "cdefghijklmnopqrstuvwxyzab"

table = maketrans(in_table, out_table) # create table for use with string.translate()

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print text.translate(table)
