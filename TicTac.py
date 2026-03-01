class TicTac: 
    x_win=0
    o_win=0
    board=[["1","2","3"],["4","5","6"],["7","8","9"]]
    combinations=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    def get_board(self):
        print("___________")
        for i in self.board:
            print(end="|")
            for j in i:
                print(j,end="|")
            print()
        print("---------")

    def get_yozish(self,index,symbol):
        index=index-1
        x=index//3
        y=index%3 
        self.board[x][y]=symbol
   
    def is_empyt(self,index):
        index=index-1
        x=index//3
        y=index%3 
        return self.board[x][y].isdigit() 

    def check_winner(self):   
        for i in self.combinations:
            x_count=0
            o_count=0
            for j in i:
                j=j-1
                x=j//3
                y=j%3
 
                if self.board[x][y] =="x":
                    x_count+=1
                elif self.board[x][y]=="o":
                   o_count+=1
            if x_count==3:
                return "x"    
            elif o_count==3:
                return "o"
        return ""

          

    def control(self):
        flag=True
        while flag:
            self.get_board()
            x_input=int(input("X ni yozish uchun joylashuvni kiriting: "))
            while not self.is_empyt(x_input):
                print("Bu joy band")
                x_input=int(input("X ni yozish uchun joylashuvni kiriting: "))
            self.get_yozish(x_input,"x")
            self.get_board()
            if self.check_winner()=="x":
                print("X g'olib")
                flag=False
                break 

            o_input=int(input("O ni yozish uchun joylashuvni kiriting:"))
            while not self.is_empyt(o_input):
               print("Bu joy band")
               o_input=int(input("O ni yozish uchun joylashuvni kiriting:"))
            self.get_yozish(o_input,"o")
            if self.check_winner()=="o":
                print("O g'olib")
                flag==False
                break

            self.check_winner()
           


game=TicTac()
game.control()