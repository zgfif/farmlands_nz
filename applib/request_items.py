import requests



class RequestItems:
    def __init__(self) -> None:
        self._items = []


    def perform(self) -> dict:
        url = "https://shop.farmlands.co.nz/search?q=handle:%22lamb-feeder-bucket-7-teat-10l%22%20OR%20handle:%22meal-feeder-poly-cone-55kg%22%20OR%20handle:%22trivox-sheep-himin-20l%22%20OR%20handle:%22milligans-multi-milk-replacer-20kg%22%20OR%20handle:%22milligans-classic-calf-milk-replacer-20kg%22%20OR%20handle:%22nrm-moozlee-20kg%22%20OR%20handle:%22reliance-calf-grower-20-25kg%22%20OR%20handle:%22ngahiwi-premium-calf-milk-replacer-20kg%22%20OR%20handle:%22milk-bar-calf-feeder-1%22%20OR%20handle:%22crystalyx-easy-breather-5kg%22%20OR%20handle:%22ahd-iodine-tincture-8-750ml%22%20OR%20handle:%22reliance-calf-2000-pellets-25kg%22%20OR%20handle:%22stallion-calf-feeder-teat-cap-threaded-peach%22%20OR%20handle:%22nrm-growup-16-protein-pellets-20kg%22%20OR%20handle:%22antahi-trusti-tuber%22%20OR%20handle:%22salt-block-saver-little-giant%22%20OR%20handle:%22stallion-5-teat-compartment-feeder-25l%22%20OR%20handle:%22antahi-refractometer-brix%22%20OR%20handle:%22milk-bar-teat-round-hole%22%20OR%20handle:%22stallion-meal-trough-free-standing-150l%22%20OR%20handle:%22shoof-farmhand-prodder-battery-powered-57cm-yellow%22%20OR%20handle:%22milk-bar-10-1-teat-pack%22%20OR%20handle:%22milk-bar-calf-screw-cap-10-packet%22%20OR%20handle:%22milk-bar-calf-feeder-5%22%20OR%20handle:%22milk-bar-calf-feeder-12%22%20OR%20handle:%22milk-bar-automatic-feeder-calf-teat%22%20OR%20handle:%22milk-bar-calf-feeder-5-teat-with-ezi-lock-hooks%22%20OR%20handle:%22antahi-trusti-tuber-starter-pack-2-in1%22%20OR%20handle:%22antahi-flexi-tuber-starter-pack-2-in1%22%20OR%20handle:%22antahi-feeder-and-teat-cap%22%20OR%20handle:%22stallion-calfateria-fence-15-teat-110l%22%20OR%20handle:%22procalf-5l-with-drench-gun%22%20OR%20handle:%22nrm-growup-20-protein-pellets-20kg%22%20OR%20handle:%22milk-bar-snack-water-trough%22%20OR%20handle:%22isl-fusion-drencher-50ml-complete%22%20OR%20handle:%22milligans-excel-plus-calf-milk-replacer-20kg%22%20OR%20handle:%22nrm-peck-n-lay-pellets-10kg%22%20OR%20handle:%22nrm-pecking-block-2-5kg%22%20OR%20handle:%22top-paddock-heavy-duty-pigtail-8mm-x-850mm-10-pack%22%20OR%20handle:%22top-paddock-offset-pigtail-175mm-5-pack%22%20OR%20handle:%22top-paddock-pigtail-10-pack-6mm-x-755mm%22%20OR%20handle:%22top-paddock-recycled-rubber-tub-30l%22%20OR%20handle:%221972-george-merino-rugby-polo-wmns%22%20OR%20handle:%221972-logan-nz-merino-1-4-zip-jumper-mns%22&type=product&view=bss.product.labels"

        response = requests.get(url=url)
        
        response.raise_for_status()
        
        return response.json()
        


