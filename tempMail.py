import guerrillamail as g


def getVerify():
    session = g.GuerrillaMailSession()
    session_id = session.session_id
    print(session_id)
    session.set_email_address("edapwwbt@guerrillamailblock.com")
    print(session.get_session_state()['email_address'])
    print("Number of Emails: ",len(session.get_email_list()))
    guid = session.get_email_list()[0].guid
    email = session.get_email(guid)

    return email.body
