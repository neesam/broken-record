from ..config.mysqlconnection import connectToMySQL

class Seventy:
    db = 'rym'
    def __init__(self, data):
        self.input_access_token = data['input_access_token']
        self.input_market = data['input_market']
        self.input_type = data['input_type']
        self.input_query = data['input_query']
        self.input_offset = data['input_offset']
        self.albums_items_album_type = data['albums_items_album_type']
        self.albums_items_artists_0_external_urls_spotify = data['albums_items_artists_0_external_urls_spotify']
        self.albums_items_artists_0_href = data['albums_items_artists_0_href']
        self.albums_items_artists_0_id = data['albums_items_artists_0_id']
        self.albums_items_artists_0_name = data['albums_items_artists_0_name']
        self.albums_items_artists_0_type = data['albums_items_artists_0_type']
        self.albums_items_artists_0_uri = data['albums_items_artists_0_uri']
        self.albums_items_external_urls_spotify = data['albums_items_external_urls_spotify']
        self.albums_items_href = data['albums_items_href']
        self.albums_items_id = data['albums_items_id']
        self.albums_items_images_0_height = data['albums_items_images_0_height']
        self.albums_items_images_0_url = data['albums_items_images_0_url']
        self.albums_items_images_0_width = data['albums_items_images_0_width']
        self.albums_items_name = data['albums_items_name']
        self.albums_items_release_date = data['albums_items_release_date']
        self.albums_items_release_date_precision = data['albums_items_release_date_precision']
        self.albums_items_total_tracks = data['albums_items_total_tracks']
        self.albums_items_type = data['albums_items_type']
        self.albums_items_uri = data['albums_items_uri']
        self.albums_href = data['albums_href']
        self.albums_limit = data['albums_limit']
        self.albums_next = data['albums_next']
        self.albums_offset = data['albums_offset']
        self.albums_previous = data['albums_previous']
        self.albums_total = data['albums_total']

    @classmethod

    def get_seventy(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1970.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventy_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1970.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyone(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1971.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyone_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1971.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventytwo(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1972.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventytwo_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1972.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventythree(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1973.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventythree_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1973.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyfour(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1974.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyfour_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1974.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyfive(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1975.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyfive_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1975.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventysix(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1976.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventysix_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1976.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyseven(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1977.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyseven_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1977.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventyeight(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1978.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventyeight_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1978.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_seventynine(cls):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1979.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_seventynine_by_id(cls, data):

        query = 'SELECT * FROM seventies_years WHERE input_query = "1979.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eighty(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1980" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eighty_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1980" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightyone(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1981" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightyone_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1981" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)

        return cls(results[0])

    @classmethod

    def get_eightytwo(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1982" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightytwo_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1982" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightythree(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1983" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightythree_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1983" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightyfour(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1984" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightyfour_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1984" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightyfive(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1985" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightyfive_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1985" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightysix(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1986" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightysix_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1986" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightyseven(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1987" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightyseven_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1987" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightyeight(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1988" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightyeight_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1988" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_eightynine(cls):

        query = 'SELECT * FROM eighties_years WHERE input_query = "1989" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_eightynine_by_id(cls, data):

        query = 'SELECT * FROM eighties_years WHERE  input_query = "1989" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninety(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1990.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninety_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1990.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetyone(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1991.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetyone_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1991.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetytwo(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1992.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetytwo_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1992.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetythree(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1993.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetythree_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1993.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetyfour(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1994.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetyfour_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1994.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetyfive(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1995.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetyfive_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1995.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetysix(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1996.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetysix_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1996.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetyseven(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1997.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetyseven_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1997.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetyeight(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1998.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetyeight_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1998.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_ninetynine(cls):

        query = 'SELECT * FROM nineties_years WHERE input_query = "1999.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_ninetynine_by_id(cls, data):

        query = 'SELECT * FROM nineties_years WHERE  input_query = "1999.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousand(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2000.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousand_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2000.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandone(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2001.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandone_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2001.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandtwo(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2002.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandtwo_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2002.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandthree(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2003.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandthree_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2003.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandfour(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2004.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandfour_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2004.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandfive(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2005.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandfive_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2005.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandsix(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2006.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandsix_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2006.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandseven(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2007.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandseven_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2007.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandeight(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2008.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandeight_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2008.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandnine(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2009.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandnine_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2009.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandten(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2010.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandten_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2010.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandeleven(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2011.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandeleven_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2011.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandtwelve(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2012.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandtwelve_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2012.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandthirteen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2013.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandthirteen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2013.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandfourteen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2014.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandfourteen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2014.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandfifteen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2015.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandfifteen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2015.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandsixteen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2016.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandsixteen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2016.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandseventeen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2017.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandseventeen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2017.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandeighteen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2018.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandeighteen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2018.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])

    @classmethod

    def get_twothousandnineteen(cls):

        query = 'SELECT * FROM twenties_years WHERE input_query = "2019.0" ORDER BY RAND()'

        return connectToMySQL(cls.db).query_db(query)

    @classmethod

    def get_twothousandnineteen_by_id(cls, data):

        query = 'SELECT * FROM twenties_years WHERE  input_query = "2019.0" and albums_items_id = %(id)s' 

        results = connectToMySQL(cls.db).query_db(query, data)

        return cls(results[0])