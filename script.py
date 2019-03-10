from selenium import webdriver
from time import sleep
import queries_to_db


browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com')



def getPolicies(number):
    print("Got Request\nFetching Data")
    text_box = browser.find_element_by_class_name("_2S1VP")
    response = "Let me fetch your policies:\n"
    text_box.send_keys(response)
    policies = queries_to_db.show_policy_by_no(number)
    if len(policies) is 0:
        text_box.send_keys("Sorry you don't have any existing policies.\n")
    else:
        for policy in policies:
            string_to_show="".join(["-"]*36)+"\n"
            string_to_show+="Plan_name : "+str(policy.plan_id)+"\n"
            if(policy.premium_amount!=None):
                string_to_show += "Premium_Amount : " + str(policy.premium_amount)+"\n"
            string_to_show+="Created_on : "+str(policy.created_on)+"\n"
            string_to_show+="".join(["-"]*36) + "\n"
            text_box.send_keys(string_to_show)
            sleep(2)  # A 1 second pause so that the program doesn't run too fast




bot_users = {} # A dictionary that stores all the users that sent activate bot 
while True:
    unread = browser.find_elements_by_class_name("OUeyt")
    name,message  = '',''
    if len(unread) > 0:
        ele = unread[-1]
        action = webdriver.common.action_chains.ActionChains(browser)
        action.move_to_element_with_offset(ele, 0, -20)
        
        try:
            action.click()
            action.perform()
            action.click()
            action.perform()
        except Exception as e:
            pass
        try:
            name = browser.find_element_by_class_name("_2zCDG").text  # Contact name
            message = browser.find_elements_by_class_name("vW7d1")[-1]  # the message content
            if 'hi acker' in message.text.lower():
                if name not in bot_users:
                    bot_users[name] = True
                    text_box = browser.find_element_by_class_name("_2S1VP")
                    response = "Hi "+name[4:].replace(" ","")+". Acko's Bot here . Now I am activated for you\n"
                    text_box.send_keys(response)
                else:
                    text_box = browser.find_element_by_class_name("_2S1VP")
                    response = "Hi " + name[4:].replace(" ", "") + ". Welcome back to acko's bot . \n"
                    text_box.send_keys(response)


            if name in bot_users:
                if 'show' in message.text.lower() and 'policy' in message.text.lower():
                    getPolicies(name[4:].replace(" ",""))
                if 'deactivate' in message.text.lower():
                    if name in bot_users:
                        text_box = browser.find_element_by_class_name("_2S1VP")
                        response = "Bye "+name+". We will miss you. \n"
                        text_box.send_keys(response)
                    del bot_users[name]


        except Exception as e:
            print(e)
            pass

