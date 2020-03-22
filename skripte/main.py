import os
import shutil

def main():
     f=open("index.txt", "r")
     fl =f.readlines()
     for x in fl:
       link = x.replace('\n', '')
       x = x.split("_")
       nr = x[slice(5, 6)]
       nr[0] = nr[0].strip('()')
       datum = x[slice(6, 9)]
       txt = x[9::]
       txt = ' '.join(txt)
       name = txt.replace('.mp3', '').replace('.ogg', '').replace('.flac', '').replace('\n', '')
       long = name.replace(' ', '-')
       long = long.lower()
       tag = '%s' % (datum[2])
       monat = '%s' % (datum[1])
       jahr = '%s' % (datum[0])
       nr = '%s' % (nr[0])
       
####### markdownfile erzeugen
       mdname = 'sfdvw%s.md' % (nr) 
       f= open(mdname,"w+")
       f=open(mdname,"a+")
       f.write("---\r\n")
       f.write("date: \"" + datum[0] + "-" + datum[1] + "-" + datum[2] + "T00:20:00+02:00\"\r\n")
       f.write("publishdate: \"" + datum[0] + "-" + datum[1] + "-" + datum[2] +  "+20:00\"\r\n")
       f.write("lastmod: \"" + datum[0] + "-" + datum[1] + "-" + datum[2] + "+20:00\"\r\n")
       f.write("draft: false\r\n")
       f.write("title: \"SfdvW - " + nr + " - " + name + "\"\r\n")
       f.write("tags: [\"\"]\r\n")
       f.write("series: [\"SfdvW\"]\r\n")
       f.write("categories: [\"Sendebeitrag\"]\r\n")
       f.write("img: \"\"\r\n")
       f.write("toc: true\r\n")
       f.write("summary: \"Sendung Nummer %s %s\"\r\n" % (nr, name))
       f.write("link: \"%s\"\r\n" % (link))
       f.write("audio: \"%s\"\r\n" % (link))
       f.write("---\r\n")
       f.write("\r\n")
       f.write("<div align=\"center\" id=\"example\"></div>\r\n")
       f.write("<script src=\"https://cdn.podlove.org/web-player/embed.js\"></script>\r\n")
       f.write("\r\n")
       f.write("Feedback zur Sendung?\r\n")
       f.write("[Schreibe uns ein Kommentar](mailto:SfdvW@radiocorax.de)\r\n")
       f.write("\r\n")
       f.write("## SfdvW - %s - %s\r\n" % (nr, name))
       f.write("mit dabei: tmk, markus, nilo, jotilux\r\n")
       f.write("\r\n")
       f.write("\r\n")
       f.write("<script>\r\n")
       f.write("  podlovePlayer(\'#example\', \'/blog/sfdvw" + nr + ".json\');\r\n")
       f.write("</script>\r\n")
       f.close()   
       
####### jsonfile erzeugen
       f=open("sfdvwMUSTER.json", "r")
       fl =f.readlines()
       jsonname = 'sfdvw%s.json' % (nr)
       f= open(jsonname,"w+")
       f=open(jsonname,"a+")
       for x in fl:
         x = x.replace('#nr', nr).replace('#name', name).replace('#tag', tag).replace('#monat', monat).replace('#jahr', jahr).replace('#long', long).replace('#link', link)
         f.write(x)
       f.close()
####### Bild erzeugen
       os.system('sh mkpic.sh %s' % (nr))

####### Dateien verschieben
       shutil.move('%s' % (mdname), "../content/blog/%s" % (mdname))
       shutil.move('%s' % (jsonname), "../content/blog/%s" % (jsonname))
       shutil.move("sfdvw%s.jpg" % (nr), "../static/img/blog/sfdvw%s.jpg" % (nr))

if __name__== "__main__":
  main()
