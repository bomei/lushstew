ETH又有点什么呢？
===

ETH是所谓的区块链2.0，与比特币的区别在于ETH的每个节点运行一个虚拟机（EVM）。ETH通过[solidity](https://solidity.readthedocs.io/en/develop/)（类似`javascript`）来编写合约（contract）。ETH的contract中既可以存储常量，也可以存储函数，用户可以通过这些函数来改变合约的状态（如，改变某个变量的值等），或是做出比较复杂的操作，这使得eth可以做出比btc复杂的东西来。

ETH去中心化的计算会带来速度和消耗的增加，但在一部人看来，比起去中心化的优点来说，这些确定完全可以接受。


### 1.ERC20
ERC20 中给出了一个在eth中实现token的标准接口。
```js
 1 // ERC Token Standard #20 Interface
 2 // https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md
 3 // ----------------------------------------------------------------------------
 4 contract ERC20Interface {
 5     function totalSupply() public constant returns (uint);
 6     function balanceOf(address tokenOwner) public constant returns (uint balance);
 7     function allowance(address tokenOwner, address spender) public constant returns (uint remaining);
 8     function transfer(address to, uint tokens) public returns (bool success);
 9     function approve(address spender, uint tokens) public returns (bool success);
10     function transferFrom(address from, address to, uint tokens) public returns (bool success);
11 
12     event Transfer(address indexed from, address indexed to, uint tokens);
13     event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
14 }
```




所谓实现token，也就是相当于发行一种新币了。Token的合约写起来简单，简单的比如[metacoin](https://github.com/truffle-box/metacoin-box/blob/master/contracts/MetaCoin.sol)，或者更加完善的如[FirstBlood Token](./src/firstbloodcoin.sol)。

发行token经常用于众筹，但是目前除了ICO没有发现很明确的应用途径。今天ICO，明天富家翁。

### 2.METAMASK
Chrome有一个插件叫`metamask`，是一个插件式的eth钱包，可以接入eth主网，测试网，或者本地网。

### 3.truffle

[Truffle](https://github.com/trufflesuite/truffle) is a development environment, testing framework and asset pipeline for Ethereum, aiming to make life as an Ethereum developer easier.

配合[ganache-cli(之前叫testrpc)](https://github.com/trufflesuite/ganache-cli)，可以很方便的搭建一个本地开发测试环境。