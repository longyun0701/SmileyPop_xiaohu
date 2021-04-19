#include<iostream>
#include<cstdlib>
#include<ctime> 
using namespace std;

int game(int h1,int h2){
	int a=1,b,ae=0,be=0,n,flag=1;
	
	while(h1>0&&h2>0&&a){
		srand(time(0));
		b=rand()%7+2;
		n=rand()%4+1;
		if(b==2&&n==1)	b=1;
		cout<<"请输入（1：能量  2：小刀 3：冲击波 4：炸弹 0：退出）\n";
		cin>>a;
		if(a==9){
			cout<<"游戏规则：\n	小刀：1能量\n	冲击波：4能量\n	炸弹：7能量\n\n";
			cout<<"请输入（1：能量  2：小刀 3：冲击波 4：炸弹 0：退出）\n";
			cin>>a;
		}
		switch(b){
			case 1:cout<<"计算机出了1\n";be++;break;
			case 2:
			case 3:if(be>=1){
					cout<<"计算机出了2\n";be--;b=2;break;	
				}
				else{
					cout<<"计算机出了1\n";be++;b=1;break;
				};break;
			case 4:
			case 5:
			case 6:	if(be>=4){
					cout<<"计算机出了3\n";be-=4;b=3;break;	
				}
				else{
					cout<<"计算机出了1\n";be++;b=1;break;
				};break;
			case 7:
			case 8:if(be>=7){
					cout<<"计算机出了4\n";be-=7;b=4;break;	
				}
				else{
					cout<<"计算机出了1\n";be++;b=1;break;
				};	break;
		}
		switch(a){
			case 1:
				ae++;
				switch(b){
				case 2:cout<<"你-1滴血!\n";h1-=1;break;
				case 3:cout<<"你-4滴血!!\n";h1-=4;ae/=2;break;
				case 4:cout<<"你-7滴血!!!\n";h1-=7;ae/=2;break;
				default:cout<<"平局\n";break;
			}break; 
			case 2:
				if(ae>=1){
				ae--;
				switch(b){
				case 2:cout<<"平局\n";break;
				case 3:cout<<"你-4滴血!!\n";h1-=4;ae/=2;break;
				case 4:cout<<"你-7滴血!!!\n";h1-=7;ae/=2;break;
				default:cout<<"计算机-1滴血\n";h2-=1;break;
				}}
				else{
					cout<<"你犯规!你只有"<<ae<<"能量。\n";
					h1--;
				}break; 
			case 3:if(ae>=4){
				ae-=4;
				switch(b){
				//case 2:cout<<"平局\n";h1-=1;break;
				case 3:cout<<"平局\n";break;
				case 4:cout<<"你-7滴血!!!\n";h1-=7;ae/=2;break;
				default:cout<<"计算机-4滴血\n";h2-=4;be/=2;break;
				}}
				else{
					cout<<"你犯规!你只有"<<ae<<"能量。\n";
					h1--;
				}break; 
			case 4:if(ae>=7){
				ae-=7;
				switch(b){
				//case 2:cout<<"平局\n";h1-=1;break;
				//case 3:cout<<"平局\n";break;
				case 4:cout<<"轰！\n";h1-=7;h2-=7;ae=be=0;break;
				default:cout<<"计算机-7滴血\n";h2-=7;be/=2;break;
				}}
				else{
					cout<<"你犯规!你只有"<<ae<<"能量。\n";
					h1--;
				}break; 
			default:cout<<"\n似乎有点BUG……";return 0;
		}
		cout<<"你的血量："<<h1<<"    计算机的血量："<<h2<<"	你有"<<ae<<"能量	计算机有"<<be<<"能量。"<<endl<<endl<<"-------------------------------"<<endl<<endl; 
		if(ae>8){
			cout<<"你自爆了！!";
			ae=0;
			h1=0;
		}
	}
	cout<<"开始自救！\n\n";
	h1+=ae;
	h1-=be/2;
	h2+=be;
	h2-=ae/2;
	cout<<"你的血量："<<h1<<"    计算机的血量："<<h2<<endl<<endl; 
	
	if(h1>0&&h2>0){
		cout<<"自救成功！\n\n---------------------------\n\n";
		flag=game(h1,h2);
	}
	
	system("pause");
	system("cls");
	if(h2<=0&&h1>0)	{
		system("color 0a");
		cout<<"恭喜你，你赢了！\n--------------------------------\n";
		flag=0;
		}
	else if(h1<=0&&h2>0)	{
		system("color 0c");
		cout<<"很抱歉，你输了。你没能成功自救。\n";
		flag=0;}
	
	
	return flag;
	
	//return 0;
}
int main(){
	int i;
	system("cls");
	cout<<"欢迎来到能量游戏\n查看游戏规则按9键。";
	cout<<"游戏规则：\n	小刀：1能量\n	冲击波：4能量\n	炸弹：7能量\n\n";
	i=game(10,10);
	if(i){
		system("color 0f");
		cout<<"打平了";
	}
	return 0;
}
