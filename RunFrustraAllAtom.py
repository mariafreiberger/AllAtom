import os
import sys


#----------Create Directories and copy files----------
mkdir='mkdir '+sys.argv[1]+'.done'
os.system(mkdir)
cp='cp job.sh '+sys.argv[1]+'.done/job.sh'
os.system(cp)
cp='cp Frust_Post_public.py '+sys.argv[1]+'.done/Frust_Post_public.py'
os.system(cp)
cp='cp RandSeq.py '+sys.argv[1]+'.done/RandSeq.py'
os.system(cp)
cp='cp native.xml '+sys.argv[1]+'.done/native.xml'
os.system(cp)
cp='cp test.xml '+sys.argv[1]+'.done/test.xml'
os.system(cp)
cp='cp '+sys.argv[1]+' '+sys.argv[1]+'.done/'+sys.argv[1]
os.system(cp)


mkdir='mkdir '+sys.argv[1]+'.done/Decoys'
os.system(mkdir)
mkdir='mkdir '+sys.argv[1]+'.done/VisualizationScript'
os.system(mkdir)
cp='cp draw_links.py '+sys.argv[1]+'.done/VisualizationScript/draw_links.py'
os.system(cp)
mkdir='mkdir '+sys.argv[1]+'.done/FrustratioData'
os.system(mkdir)

os.system('python genera_xml.py '+sys.argv[1]+' '+sys.argv[3]+' '+sys.argv[4])


#--------Runing FrustraAllAtom------
job_frustra='cd '+sys.argv[1]+'.done;./job.sh '+sys.argv[1]+' '+sys.argv[2]
os.system(job_frustra)
os.system('cd '+sys.argv[1]+'.done;chmod +x job.sh')

#--- Moving files-----

mv='cd '+sys.argv[1]+'.done;mv *.log* Decoys/'
os.system(mv)
mv='cd '+sys.argv[1]+'.done;mv *.pdb* Decoys/'
os.system(mv)
mv='cd '+sys.argv[1]+'.done;mv *.dat* FrustratioData/'
os.system(mv)
mv='cd '+sys.argv[1]+'.done;mv tertiary_frustration.pml VisualizationScript/tertiary_frustration.pml'
os.system(mv)
mv='cd '+sys.argv[1]+'.done;mv tertiary_frustration.tcl VisualizationScript/tertiary_frustration.tcl'
os.system(mv)
cp='cp '+sys.argv[1]+'.done/Decoys/'+sys.argv[1]+' '+sys.argv[1]+'.done/VisualizationScript/'+sys.argv[1]
os.system(cp)

out=open(sys.argv[1]+'.done/VisualizationScript/tertiary_frustration.pml','r+')
out.write('load '+sys.argv[1]+'\n')
out.close()
