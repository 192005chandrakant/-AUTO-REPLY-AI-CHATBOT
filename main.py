import pyautogui
import time
import pyperclip
import google.generativeai as genai

def is_last_message_from_sender(chat_log, sender_name="sender_name"):
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False



pyautogui.click(1348, 1062)

time.sleep(2)  
while True:
    time.sleep(5)
   
    pyautogui.moveTo(749, 220)
    pyautogui.dragTo(1852, 898, duration=2.0, button='left')  
   
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2) 
    pyautogui.click(1258, 587)

    
    chat_history = pyperclip.paste()

  
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
          genai.configure(api_key="AIzaSyBvuUMOlJ13MhAueiG3dbIbod1TeMcRaZA")  
          model = genai.GenerativeModel("gemini-1.5-flash")
      
          response = model.generate_content(f'''You are Chandrakant, a bilingual coder from India who speaks Hindi and English. Respond to questions based solely on the provided chat history.

           Maintain a conversational tone, like a human chatting on WhatsApp.
           Do not generate additional custom output or make up information outside the chat history.
           Keep responses concise and friendly unless the question demands detail.
           Chat History: {chat_history}''')

       

          try:
               assistant_response = response.text
               print("Generated response:", assistant_response)

          
               pyperclip.copy(assistant_response)

           
               pyautogui.click(951,958)
               time.sleep(1)  

          
               pyautogui.hotkey('ctrl', 'v')
               time.sleep(1) 
               pyautogui.press('enter')
          except Exception as e:
                print(f"Error generating response: {e}")
