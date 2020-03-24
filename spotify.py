import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
client_id = '6dcde59a3750426cbe4001fdec7a02a9'
client_secret = 'e3394251d81b44e19714acfa3da7c8ed'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API


def convertMillis(millis):
     seconds=(millis/1000)%60
     minutes=(millis/(1000*60))%60
     hours=(millis/(1000*60*60))%24
     #return seconds, minutes, hours
     return "%d:%d" % (minutes,seconds)

def main():
    csvfile=open('persons.csv','w', newline='')
    csvwriter=csv.writer(csvfile)

    csvfileReader=open('Mumford-Catalogue.csv','r', newline='')
    obj=csv.reader(csvfileReader)
    next(obj)
    for row in obj:
        if len(row[0])==0:
            continue
        art_name = row[0] #"Paul Mumford"
        abm_name=row[1] #"sunrise"

        search_query = "artist:" + art_name + " "
        search_query = "artist:\"%s\" album:\"%s\"" % (art_name, abm_name)

        print (search_query)
        #print(row)
        #continue;
        results = sp.search(q=search_query, limit=20) #search query

        csvwriter.writerow("")
        csvwriter.writerow( (art_name, abm_name, results['tracks']['total']) )
        # albums= "Sunrise"
        

        for idx, track in enumerate(results['tracks']['items']):
            t_len= convertMillis( track['duration_ms'] )
            t_id=track['id']
            t_name=track['name']
            t_line=" %s, %s, %s" % (t_name, t_len, t_name)
            # write to csv
            csvwriter.writerow( (t_name, t_len, t_name) )

    csvfile.close()

main()
