def login(self):
                
                
                userdat = json.loads(ConnectFtp.GetuserData().getvalue())
                user_text = self.loginWindow.UserNameEN.text()
                user = hashlib.sha512(self.loginWindow.UserNameEN.text().encode()).hexdigest()
                password =  hashlib.sha512(self.loginWindow.PasswordEN.text().encode()).hexdigest()
               
                try:
                        
                        if userdat[user]["password"] == password:
                                
                                # global Current
                                # Current = user_text
                                CurrentUserName = user_text
                                print("UI Started")
                                self.StartMainUi()
                                
                               
                        else:
                                
                                QMessageBox.critical(self, "Error", "Wrong password")
                                # self.loginWindow.PasswordEN.setText("")
                                print("incorrect passwrod")
                                return
                except:
                        
                        QMessageBox.critical(self, "Error", "An error has occurred")
                        self.loginWindow.UserNameEN.setText("")
                        self.loginWindow.PasswordEN.setText("")   

