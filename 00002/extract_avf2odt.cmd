rem Lokasi program OOMMF.
set oommf="C:\euphoberia\fept\oommf\v2.1a2\oommf.tcl"

rem Wilayah geometri yang nilai magnetisasinya
rem ingin diekstrak.
set xfrom=0e-9
set xto=150e-9
set yfrom=0e-9
set yto=50e-9
set zfrom=0e-9
set zto=10e-9

rem Folder tempat file-file OMF disimpan.
set basedir="C:\euphoberia\nife\obs\02511.00004\v0\00002\materi\n-3.shell-6.ms-8e5"

rem Nama file luaran
set outfile="film_tipis.odt"

tclsh %oommf% avf2odt -region %xfrom% %yfrom% %zfrom% %xto% %yto% %zto% -ipat %basedir%/*.omf -onefile %basedir%/%outfile% -normalize 1 -header none