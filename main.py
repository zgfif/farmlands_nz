from applib.collect_data import CollectData



def main() -> None:
    url = 'https://shop.farmlands.co.nz/collections/animal-type-calf'
    CollectData(url=url).perform()



if __name__ == '__main__':
    main()
