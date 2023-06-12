#!/usr/bin/python3

if __name__ != "__main__":

    males = ("Beckett","Carsen","Marcel","Dennis","Leonard","Kayden","Milo","Luke","Coleman","Yusuf","Francisco","Finley")
    females = ("Kennedi","Jaylee","Esther","Elisa","Gabrielle","Kathryn","Dayanara","Leslie","Joy","Jillian","Avery","Daniela")
    phone = ("(408) 772-0477","(651) 752-4105","(205) 635-5522","(739) 939-9404","(453) 208-2004","(572) 923-1849","(894) 773-3032","(565) 390-5516","(452) 314-9582","(256) 344-3740","(523) 707-4764","(735) 973-8939","(832) 897-5203","(877) 396-0870","(772) 905-4101","(897) 893-5108","(627) 461-1724","(456) 421-7949","(936) 792-1270","(485) 895-4274","(206) 743-2866","(371) 388-9325","(232) 648-2544","(879) 617-9280")
    address = ("9141 Henry Smith Lane","Bardstown, KY 40004","62 High Street","Fall River, MA 02720","15 Mammoth Lane","Ozone Park, NY 11417","9512 Holly Street","North Haven, CT 06473","69 Hawthorne Street","Middleburg, FL 32068","385 William Ave.","Cleveland, TN 37312","31 S. Pine Court","Clemmons, NC 27012","9493 Golden Star Ave.","Pearl, MS 39208","341 New Saddle St.","Warner Robins, GA 31088","22 Madison Circle","Corpus Christi, TX 78418","23 Myers Court","Elmhurst, NY 11373","349 Thomas Circle","Hightstown, NJ 08520","1 Ryan Lane","Grand Forks, ND 58201","912 Snake Hill Lane","Severna Park, MD 21146","7834 Bow Ridge Street","New Philadelphia, OH 44663","9937 Penn Street","Marcus Hook, PA 19061","80 Cedar Swamp Avenue","Randallstown, MD 21133","23 S. Albany St.","Halethorpe, MD 21227","52 Glendale Drive","Ames, IA 50010","7017 Miles Circle","Midland, MI 48640","1 West Windsor Ave.","South Windsor, CT 06074","37 Edgemont Ave.","Windsor, CT 06095","91 Ryan Street","Stratford, CT 06614","8362 Hudson Street","Stroudsburg, PA 18360")
    email = ("carreras@live.com","jyoliver@sbcglobal.net","dexter@icloud.com","cosimo@yahoo.ca","dmath@me.com","jguyer@aol.com","squirrel@sbcglobal.net","presoff@msn.com","mstrout@me.com","mlewan@aol.com","jsnover@outlook.com","aglassis@mac.com","miltchev@sbcglobal.net","ahmad@icloud.com","dexter@comcast.net","yxing@optonline.net","mastinfo@hotmail.com","staffelb@mac.com","luvirini@comcast.net","hutton@me.com","wildfire@comcast.net","mddallara@yahoo.com","gomor@sbcglobal.net","osrin@gmail.com")
    zip_code = ("15401 Uniontown, PA","08701 Lakewood, NJ","52240 Iowa City, IA","24112 Martinsville, VA","60101 Addison, IL","29576 Murrells Inlet, SC","29710 Clover, SC","06770 Naugatuck, CT","18062 Macungie, PA","49428 Jenison, MI","20109 Manassas, VA","11570 Rockville Centre, NY","01880 Wakefield, MA","37122 Mount Juliet, TN","65401 Rolla, MO","48423 Davison, MI","07011 Clifton, NJ","56301 Saint Cloud, MN","44221 Cuyahoga Falls, OH","74403 Muskogee, OK","07712 Asbury Park, NJ","01604 Worcester, MA","18702 Wilkes Barre, PA","30281 Stockbridge, GA")

    names = list(zip(males,females))

    class People:
        def __init__(self) -> None:
            self._name = name
            self._email = email
            self._phone = phone
            self._zip = code
            self._address = address

        def get_info(self):
            print("\n\tName: {}\n\tEmail: {}\n\tPhone: {}\n\tZip Code: {}\n\tAddress: {}".format(
                self._name,
                self._email,
                self._phone,
                self._address,
                self._zip))
