class Parser(object):

    @staticmethod
    def parse_fit(eft):
        """
        Fit parser for the 'Fitting Calculator'. This takes an EFT formatted fit and parses it into a usable list of
        entities to price. This function dictates the flow of the parser
        :param eft: EvE Fitting Tool (Standard EvE fit format)
        :return: Dictionary containing quantity required for each entity using the format: {entity: quantity}
        """
        shopping_list = dict()
        eft_list = eft.split('\n')
        eft_list.reverse()
        try:
            shopping_list[Parser.__hull_parser(eft_list.pop())] = 1  # Adds the hull to the dictionary with quantity 1
            # TODO: Finish parser
        except Exception as e:
            # FIXME: Perform proper error handling
            pass
                    
    @staticmethod
    def __hull_parser(eft_hull):
        """
        Parses the first line in an EFT and returns the appropriate hull name
        :param eft_hull: EFT first line
        :return: Name of the ship hull as a string
        """
        hull = ''
        for i in range(1, len(eft_hull)):
            if eft_hull[i] == ',':
                return hull
            else:
                hull += eft_hull[i]

        # Code should never get this far
        raise Exception("PARSE ERROR: Fit does not follow EFT format. Parse failed on HULL.")

# Sample EFT fit for formatting
"""
[Panther, Galorndon's Panther]
Dark Blood Armor EM Hardener
Dark Blood Armor Thermal Hardener
Gyrostabilizer II
Gyrostabilizer II
Imperial Navy 1600mm Steel Plates
Imperial Navy 1600mm Steel Plates

500MN Y-T8 Compact Microwarpdrive
Fleeting Compact Stasis Webifier
Large Micro Jump Drive
Warp Scrambler II
Heavy Electrochemical Capacitor Booster I,Navy Cap Booster 3200

Dread Guristas Cloaking Device
Medium Energy Neutralizer II
Medium Energy Neutralizer II
800mm Repeating Cannon II,Hail L
800mm Repeating Cannon II,Hail L
800mm Repeating Cannon II,Hail L
800mm Repeating Cannon II,Hail L
800mm Repeating Cannon II,Hail L

Large Trimark Armor Pump II
Large Trimark Armor Pump II

Acolyte II x5
Hornet EC-300 x2
Hornet EC-300 x3
"""