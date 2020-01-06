import os


stra = "<div class=\"logos col-md-3 col-sm-6 col-xs-6\">\n"
stra+= "\t<div class=\"thumbnail\">\n"
stra+= "\t\t<img src=\"{{% static 'sponsors/sponsors_logos/{}' %}}\">\n"
stra+="\t\t<center style=\"color:white; padding: 5px;\">{}</center>\n"
stra+="\t</div>\n"
stra+="</div>\n"

for (root,dirs,files) in os.walk('.', topdown=True): 
    for f in files:
    	print(stra.format(f,f.split('.')[0]))