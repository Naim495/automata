def is_valid_email(email):
    state = 'q0'
    
    for ch in email:
        if state == 'q0':
            if ch.isalnum():
                state = 'q1'
            else:
                return False
        
        elif state == 'q1':
            if ch.isalnum() or ch in ['.', '_']:
                state = 'q1'
            elif ch == '@':
                state = 'q2'
            else:
                return False
        
        elif state == 'q2':
            if ch.isalnum():
                state = 'q2'
            elif ch == '.':
                state = 'q3'
            else:
                return False
        
        elif state == 'q3':
            if ch.isalpha():
                state = 'q_accept'
            else:
                return False
        
        elif state == 'q_accept':
            if ch.isalpha():
                state = 'q_accept'
            else:
                return False
    
    return state == 'q_accept'
