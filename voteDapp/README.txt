1:设置环境
mkdir simple_vote_dapp
npm init
npm install web3 solc ganache-cli
./node_modules/.bin/ganache-cli --help
./node_modules/.bin/ganache-cli
npm -global list 

2:设置mysql的连接权限
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';
FLUSH PRIVILEGES;

