import requests
import streamlit as st
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = '' 
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None
st.sidebar.title('AV SAAS')
if st.session_state['logged_in']:
     st.sidebar.success(f"WELCOME {st.session_state['username']}")
     st.sidebar.header('Menu')
     page = st.sidebar.radio(
     'Go To',
     [
        'Add note',
        'Read Note',
        'Update Note',
        'Delete Note',
        'Ask AI'
     ]
     )
if not st.session_state['logged_in']:    
 st.header('Login')
 login_username = st.text_input('Username',
                               key= 'login_usename')
 login_email = st.text_input('Email',
                            key='login_email')
 login_password = st.text_input('password',type='password',key='login_password')
 if st.button('Login'):
     response = requests.post(
        'https://snap-sadness-emphasis.ngrok-free.dev/login',
        json= {
            'username': login_username,
            'email': login_email,
            'password':login_password
            
        }
     )
     st.write(response.status_code)
     st.write(response.json())
     if response.status_code == 200:
         data = response.json()
         st.session_state['logged_in'] = True
         st.session_state['user_id'] = data['user_id']
         st.success('login Successfully')
         st.session_state['username'] = login_username
         st.success(f"WELCOME {st.session_state['username']}")
 st.header('Register') 
 register_username = st.text_input('Username',
                                  key='register_username')
 register_email = st.text_input('email',
                               key='register_email')
 register_password = st.text_input('password',type='password',
                                  key='register_password')
 if st.button('Register'):
     response= requests.post(
        'https://snap-sadness-emphasis.ngrok-free.dev/Register',
        json ={'username': register_username,
            'email': register_email,
            'password':register_password 
        }
     )    
     st.write('Status:',
             response.status_code)
     st.success('Registered SUCCESSFULLY')
else:
     if page == 'Add note':
         st.header('ADD NOTES')
         content_text = st.text_area('Add note here')
         if st.button('Add note'):
             response = requests.post(
                'https://snap-sadness-emphasis.ngrok-free.dev/notes',
             json = {'user_id' : st.session_state['user_id'],
                'content': content_text
             }
              )
             st.write('Status:',
             response.status_code)
             st.write(response.text)
     elif page == 'Ask AI':
         st.header('ASK AI')  
         question_input =st.text_area('Enter your question here')
         if st.button('ASK'):
             response= requests.post(
               'https://snap-sadness-emphasis.ngrok-free.dev/ask',
             json= {'user_id': st.session_state['user_id'],
                 'question': question_input
                 }
             )
             st.write(response.status_code)
             st.write(response.json())
     elif page == 'Read Note':     
         st.header('Read notes')
         if st.button('READ YOUR NOTES'):
             response = requests.get(
             'https://snap-sadness-emphasis.ngrok-free.dev/read_notes',
             params= {'user_id': st.session_state['user_id']
                     }
             )
             st.write(response.status_code)
             st.write(response.json())
     elif page == 'Update Note':     
         st.header('UPDATE NOTE')
         note_id = st.number_input('Enter your note id',min_value=1)
         update_note = st.text_input('new content')
         if st.button('Update note'):
             response=requests.put(
              'https://snap-sadness-emphasis.ngrok-free.dev/update notes',
               json = {
                'id': note_id,
                'content': update_note
               }
              )
             st.write(response.status_code)
             st.success('Note updated SUCCESSFULLY')
     elif page == 'Delete Note':     
         st.header('DELETE NOTE')
         delete_id =st.number_input('enter your note id',min_value =1,key='delete_note')
         if st.button('delete'):
             response = requests.delete(
             'https://snap-sadness-emphasis.ngrok-free.dev/Delete notes',
             params = {'delete_id':delete_id}
             )
             st.write(response.status_code)
             st.success('Note deleted successfully')
     if st.button('LOGOUT'):
         st.session_state['logged_in'] = False
         st.session_state.pop('user id',None)  
         st.rerun()
        
        
        
               
            
        
        
        
        
        
        
        
        
        

    
    