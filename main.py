# import sys
# print(sys.path)
# sys.path.append(r'C:\\Python\\flv')

from animeflv import AnimeFLV


with AnimeFLV() as api:

    elements = api.search(input("Escribe el nombre de la serie:"))
    for i, element in enumerate(elements):
        print(f"{i}, {element.title}")
        try:
            selection = int(input("Select option:"))
            info = api.get_anime_info(elements[selection].id)
            info.episodes.reverse()
            for j, episode in enumerate(info.episodes):
                print(f"{j} | Episode - {episode.id}")
            index_episode = int(input("Select episode:"))
            serie = elements[selection].id
            capitulo = info.episodes[index_episode].id
            results = api.get_links(serie, capitulo)
            for result in results:
                print(f"{result.server} - {result.url}")
            pass
        except Exception as e:
            print(e)