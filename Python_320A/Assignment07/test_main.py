'''
Tests Main.py the main driver code for Social Network
'''
# pylint: disable=redefined-outer-name, unused-import
import os
from pathlib import Path
import pytest
import main
from test_user_status import full_status_db
from test_users import empty_db

HERE = Path(__file__).parent


def test_search_user(full_status_db):
    '''
    search_user successful test
    '''
    user_col = main.init_user_collection(full_status_db)
    user = main.search_user('Tay_01', user_col)

    assert user.user_id == "Tay_01"
    assert user.email  == "Tay@email.com"
    assert user.user_name == "Tay"
    assert user.user_last_name == "Pham"

def test_search_user_fail(full_status_db):
    '''
    search_user unsuccessful test
    '''
    user_col = main.init_user_collection(full_status_db)
    user = main.search_user('Tay100',
                            user_col)

    assert user.user_id is None
    assert user.email is None
    assert user.user_name is None
    assert user.user_last_name is None

def test_add_user(full_status_db):
    '''
    add_user successful test
    '''
    user_col = main.init_user_collection(full_status_db)
    new_user = main.add_user('New_01',
                            'New_first',
                            'New_last',
                            'New@email.com',
                            user_col)

    assert new_user is True
    assert main.search_user('New_01', user_col).user_id == 'New_01'

def test_add_user_duplicate(full_status_db):
    '''
    add_user test for user already in collection
    '''
    user_col = main.init_user_collection(full_status_db)
    new_user = main.add_user("KiKi_01",
                            "Ki",
                            'Ki',
                            "Ki@email.com",
                            user_col)

    assert new_user is False
    assert len(user_col) == 3

def test_update_user(full_status_db):
    '''
    update_user successful test
    '''
    user_col = main.init_user_collection(full_status_db)
    mod_user = main.update_user\
        ("KiKi_01", "New_Ki@email.com", "New_Ki", "New_Ki", user_col)

    assert mod_user is True

    user = main.search_user("KiKi_01", user_col)

    assert user.user_id == "KiKi_01"
    assert user.email  == "New_Ki@email.com"
    assert user.user_name == "New_Ki"
    assert user.user_last_name == "New_Ki"
    assert len(user_col) == 3

def test_update_user_not_found(full_status_db):
    '''
    update_user unsuccessful test
    '''
    user_col = main.init_user_collection(full_status_db)

    mod_user = main.update_user\
        ("not_there", "New_Bear@email.com", "New_James", "New_bear", user_col)

    assert mod_user is False
    assert main.search_user("not_there", user_col).user_id is None
    assert len(user_col) == 3

def test_search_status(full_status_db):
    '''
    search_user successful test
    '''
    status_col = main.init_status_collection(full_status_db)

    status = main.search_status('Tay_01_0001',
                            status_col)

    assert status.status_id == "Tay_01_0001"
    assert status.user_id == "Tay_01"
    assert status.status_text == "This is test text."

def test_search_status_fail(full_status_db):
    '''
    search_status unsuccessful test
    '''
    status_col = main.init_status_collection(full_status_db)

    status = main.search_status('not_there',
                            status_col)

    assert status.status_id is None
    assert status.user_id is None
    assert status.status_text is None

def test_delete_user(full_status_db):
    '''
    delete_user successful test, also removes statues associated with id.
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)

    delete_user = main.delete_user("Tay_01", user_col, status_col)

    assert delete_user is True
    assert main.search_user("Tay_01", user_col).user_id is None
    assert len(user_col) == 2

    assert main.search_status("Tay_01_0001", status_col).status_id is None
    assert main.search_status("Tay_01_0002", status_col).status_id is None
    assert len(status_col) ==3

def test_delete_user_not_there(full_status_db):
    '''
    delete_user unsuccessful test
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)

    delete_user = main.delete_user("not_there", user_col, status_col)

    assert delete_user is False

def test_add_status(full_status_db):
    '''
    add_status successful test
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)

    add_user = main.add_status("James_01", "James_01_0003","3rd Status", status_col, user_col)

    assert add_user is True
    status = main.search_status("James_01_0003", status_col)
    assert status.status_id == "James_01_0003"
    assert len(status_col) == 6


def test_add_status_duplicate(full_status_db):
    '''
    add_status test for user already in collection
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)

    add_user = main.add_status("James_01", "James_01_0001","3rd Status", status_col, user_col)

    assert add_user is False
    assert len(status_col) == 5

def test_add_status_no_user(full_status_db):
    '''
    add_status test for user already in collection
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)

    add_user = main.add_status("not_there", "James_01_0003","3rd Status", status_col, user_col)

    assert add_user is False
    assert len(status_col) == 5

def test_delete_status(full_status_db):
    '''
    delete_status successful test
    '''

    status_col = main.init_status_collection(full_status_db)
    delete_status = main.delete_status('Tay_01_0001', status_col)

    assert delete_status is True
    assert main.search_status('Tay_01_0001', status_col).status_id is None


def test_delete_status_not_there(full_status_db):
    '''
    delete_status unsuccessful test
    '''
    status_col = main.init_status_collection(full_status_db)
    delete_status = main.delete_status('not_there', status_col)

    assert delete_status is False


def test_modify_status(full_status_db):
    '''
    modify_status successful test
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)
    mod_status = main.update_status("James_01_0001",\
        "James_01", "New Status Text", status_col, user_col)

    search_status = main.search_status('James_01_0001', status_col)
    assert mod_status is True
    assert search_status.status_id == 'James_01_0001'
    assert search_status.user_id == "James_01"
    assert search_status.status_text == "New Status Text"


def test_modify_status_not_found(full_status_db):
    '''
    modify_status unsuccessful test
    '''

    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)
    mod_status = main.update_status("not_there", \
        "James_01", "New Status Text", status_col, user_col)

    search_status = main.search_status("not_there", status_col)
    assert mod_status is False
    assert search_status.status_id is None
    assert search_status.user_id is None
    assert search_status.status_text is None


def test_modify_status_invalid_user_id(full_status_db):
    '''
    modify_status unsuccessful test because of user_id not found.
    '''
    user_col = main.init_user_collection(full_status_db)
    status_col = main.init_status_collection(full_status_db)
    mod_status = main.update_status("James_01_0001",\
        "not_there", "New Status Text", status_col, user_col)

    search_status = main.search_status("James_01_0001", status_col)
    assert mod_status is False
    assert search_status.status_id == 'James_01_0001'
    assert search_status.user_id == "James_01"
    assert search_status.status_text == "More Test Text."

def write_good_accounts(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
Larisa.Yesima75,Larisa,Yesima,Larisa.Yesima75@testmail.com
Danell.Genie25,Danell,Genie,Danell.Genie25@goodmail.com
Sissie.Andromede43,Sissie,Andromede,Sissie.Andromede43@testmail.com
Angy.Piselli51,Angy,Piselli,Angy.Piselli51@funmail.com
Eugenia.Eden61,Eugenia,Eden,Eugenia.Eden61@funmail.com
Jacquette.Tiphany69,Jacquette,Tiphany,Jacquette.Tiphany69@funmail.com
Quintilla.Witty8,Quintilla,Witty,Quintilla.Witty8@funmail.com
Tiphany.Herwig57,Tiphany,Herwig,Tiphany.Herwig57@testmail.com
Danit.Berni57,Danit,Berni,Danit.Berni57@funmail.com
Carina.Starks6,Carina,Starks,Carina.Starks6@testmail.com
Andy.Maryellen86,Andy,Maryellen,Andy.Maryellen86@goodmail.com
Waly.Skip64,Waly,Skip,Waly.Skip64@funmail.com
Shawn.Verena70,Shawn,Verena,Shawn.Verena70@testmail.com
Fina.Shaff79,Fina,Shaff,Fina.Shaff79@goodmail.com
Iseabal.Nuri37,Iseabal,Nuri,Iseabal.Nuri37@goodmail.com
Bevvy.Zondra50,Bevvy,Zondra,Bevvy.Zondra50@testmail.com
Brigitte.Daisi53,Brigitte,Daisi,Brigitte.Daisi53@funmail.com
Sydel.Umeko33,Sydel,Umeko,Sydel.Umeko33@funmail.com
Isadora.Finbar34,Isadora,Finbar,Isadora.Finbar34@testmail.com
Amy.Ahmad36,Amy,Ahmad,Amy.Ahmad36@funmail.com
Olivette.Malti17,Olivette,Malti,Olivette.Malti17@funmail.com
Gerrie.Sansone18,Gerrie,Sansone,Gerrie.Sansone18@goodmail.com
Maia.Penthea8,Maia,Penthea,Maia.Penthea8@funmail.com
Tamiko.Nidorf14,Tamiko,Nidorf,Tamiko.Nidorf14@testmail.com
Darya.Marsha82,Darya,Marsha,Darya.Marsha82@funmail.com
Murielle.Chapman86,Murielle,Chapman,Murielle.Chapman86@funmail.com
Kath.Deegan88,Kath,Deegan,Kath.Deegan88@goodmail.com
Libbie.Vacuva91,Libbie,Vacuva,Libbie.Vacuva91@testmail.com
Wallis.Eastman6,Wallis,Eastman,Wallis.Eastman6@funmail.com""")

def test_load_users_good(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
    If successful, it it returns True.
    This uses a "good" csv file
    """
    write_good_accounts(HERE / "good_acct.csv")
    user_col = main.init_user_collection(empty_db)
    result = main.load_users("good_acct.csv", user_col)
    os.remove(HERE / "good_acct.csv")

    assert result is True
    assert main.search_user('Murielle.Chapman86', user_col).user_id == 'Murielle.Chapman86'
    assert main.search_user('Libbie.Vacuva91', user_col).user_id == 'Libbie.Vacuva91'
    assert len(user_col) == 29

def write_bad_accounts(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,EMAIL,NAME,LASTNAME
Larisa.Yesima75,,Larisa.Yesima75@testmail.com
Danell.Genie25,Danell,Genie,Danell.Genie25@goodmail.com
Sissie.Andromede43,Sissie,Andromede,Sissie.Andromede43@testmail.com""")

def test_load_users_bad(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
        - Returns False if there are any errors
        (such as empty fields in the source CSV file)
    This uses a "bad" csv file
    """

    write_bad_accounts(HERE / "bad_acct.csv")
    user_col = main.init_user_collection(empty_db)
    result = main.load_users("bad_acct.csv", user_col)
    os.remove(HERE / "bad_acct.csv")

    assert result is False
    assert main.search_user('Larisa.Yesima75', user_col).user_id is None
    assert main.search_user('Sissie.Andromede43', user_col).user_id is None

def write_bad_headers_accounts(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,,LASTNAME,EMAIL
evmiles97,Eve,Miles,eve.miles@uw.edu
dave03,David,Yuen,david.yuen@gmail.com""")

def test_load_users_bad_header(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
        - Returns False if there are any errors
        (such as empty fields in the source CSV file)
    This uses a "bad" csv file
    """
    write_bad_headers_accounts(HERE / "bad_head.csv")
    user_col = main.init_user_collection(empty_db)
    result = main.load_users("bad_head.csv", user_col)
    os.remove(HERE / "bad_head.csv")

    assert result is False
    assert main.search_user('evmiles97', user_col).user_id is None
    assert main.search_user('dave03', user_col).user_id is None


def write_good_status(filename):
    """
    Creates a files for status_updates.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
Larisa.Yesima75_001,Larisa.Yesima75,test_status
Danell.Genie25_001,Danell.Genie25,test_status
Sissie.Andromede43_001,Sissie.Andromede43,test_status
Angy.Piselli51_001,Angy.Piselli51,test_status
Eugenia.Eden61_001,Eugenia.Eden61,test_status
Jacquette.Tiphany69_001,Jacquette.Tiphany69,test_status
Quintilla.Witty8_001,Quintilla.Witty8,test_status
Tiphany.Herwig57_001,Tiphany.Herwig57,test_status
Danit.Berni57_001,Danit.Berni57,test_status""")
    return filename

def test_load_status_updates_good(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
    If successful, it it returns True.
    This uses a "good" csv file
    """
    write_good_accounts(HERE / "good_acct.csv")
    user_col = main.init_user_collection(empty_db)
    write_good_status(HERE / "good_status.csv")
    status_col = main.init_status_collection(empty_db)

    main.load_users("good_acct.csv", user_col)
    result = main.load_status_updates("good_status.csv", status_col, user_col)

    os.remove(HERE / "good_acct.csv")
    os.remove(HERE / "good_status.csv")

    assert result is True
    assert main.search_status('Danit.Berni57_001', \
        status_col).status_id == 'Danit.Berni57_001'
    assert main.search_status('Sissie.Andromede43_001', \
        status_col).status_id == 'Sissie.Andromede43_001'
    assert main.search_status('Quintilla.Witty8_001', \
        status_col).status_id == 'Quintilla.Witty8_001'
    assert len(status_col) == 9

def write_bad_header_status(filename):
    """
    Creates a files for status_updates.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write(""",STATUS_TEXT
evmiles97_00001,evmiles97,"Code is finally compiling"
dave03_00001,dave03,"Sunny in Seattle this morning"
evmiles97_00002,evmiles97,"Perfect weather for a hike""")
    return filename

def test_load_status_bad_header(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
        - Returns False if there are any errors
        (such as empty fields in the source CSV file)
    This uses a "bad" csv file
    """
    write_good_accounts(HERE / "good_acct.csv")
    user_col = main.init_user_collection(empty_db)
    write_bad_header_status(HERE / "bad_header_status.csv")
    status_col = main.init_status_collection(empty_db)

    main.load_users("good_acct.csv", user_col)
    result = main.load_status_updates("bad_header_status.csv", status_col, user_col)

    os.remove(HERE / "good_acct.csv")
    os.remove(HERE / "bad_header_status.csv")

    assert result is False
    assert main.search_status('evmiles97_00001', status_col).status_id is None
    assert main.search_status('dave03_00001', status_col).status_id is None
    assert main.search_status('evmiles97_00002', status_col).status_id is None


# def test_load_status_no_users(empty_db):
#     '''loads status without users'''

#     write_good_status(HERE / "good_status.csv")
#     user_col = main.init_user_collection(empty_db)
#     status_col = main.init_status_collection(empty_db)
#     result = main.load_status_updates("good_status.csv", status_col, user_col)
#     os.remove(HERE / "good_status.csv")
#     assert result is True
#     assert len(status_col) == 0

def write_missing_status(filename):
    """
    Creates a files for status_updates.csv with bad extra data
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT
evmiles97_00001,evmiles97,"Code is finally compiling"
dave03_00001,dave03,"Sunny in Seattle this morning"
evmiles97_00002,,"Perfect weather for a hike""")
    return filename

def test_load_status_missing_data(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
        - Returns False if there are any errors
        (such as empty fields in the source CSV file)
    This uses a "bad" csv file
    """

    write_good_accounts(HERE / "good_acct.csv")
    user_col = main.init_user_collection(empty_db)
    write_missing_status(HERE / "bad_missing_status.csv")
    status_col = main.init_status_collection(empty_db)

    main.load_users("good_acct.csv", user_col)
    result = main.load_status_updates("bad_missing_status.csv", status_col, user_col)

    os.remove(HERE / "good_acct.csv")
    os.remove(HERE / "bad_missing_status.csv")

    assert result is False
    assert main.search_status('evmiles97_00001', status_col).status_id is None
    assert main.search_status('dave03_00001', status_col).status_id is None
    assert main.search_status('evmiles97_00002', status_col).status_id is None

def write_blank_accounts(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""USER_ID,NAME,LASTNAME,EMAIL""")

def test_load_users_blank(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
    If successful, it it returns True.
    This uses a "good" csv file
    """
    write_blank_accounts(HERE / "blank_acct.csv")
    user_col = main.init_user_collection(empty_db)
    result = main.load_users("blank_acct.csv", user_col)
    os.remove(HERE / "blank_acct.csv")

    assert result is False
    assert len(user_col) == 0

def test_load_users_invalid_file(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
    If successful, it it returns True.
    This uses a "good" csv file
    """

    user_col = main.init_user_collection(empty_db)
    result = main.load_users("not_there", user_col)

    assert result is False
    assert len(user_col) == 0

def test_load_status_invalid_file(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
        - Returns False if there are any errors
        (such as empty fields in the source CSV file)
    This uses a "bad" csv file
    """
    write_good_accounts(HERE / "good_acct.csv")
    user_col = main.init_user_collection(empty_db)
    status_col = main.init_status_collection(empty_db)
    main.load_users("good_acct.csv", user_col)
    result = main.load_status_updates("not_there", status_col, user_col)

    os.remove(HERE / "good_acct.csv")

    assert result is False

def write_blank_status(filename):
    """
    Creates a files for accounts.csv with bad headers
    """
    with open(filename, 'w', encoding='utf-8') as outfile:
        outfile.write("""STATUS_ID,USER_ID,STATUS_TEXT""")

def test_load_status_blank(empty_db):
    """
    tests : Opens a CSV file with user data and
            adds it to an existing instance of
            UserCollection
    If successful, it it returns True.
    This uses a "good" csv file
    """
    write_good_accounts(HERE / "good_acct.csv")
    write_blank_status(HERE/ 'blank_status.csv')
    user_col = main.init_user_collection(empty_db)
    status_col = main.init_status_collection(empty_db)
    main.load_users("good_acct.csv", user_col)
    result = main.load_status_updates('blank_status.csv', status_col, user_col)
    os.remove(HERE / "good_acct.csv")
    os.remove(HERE / 'blank_status.csv')

    assert result is True
    assert len(status_col) == 0
