HTML Code -

<html?>
    <body>
        <h1>This is Sneha's first dApp</h1>
        <p>Here we are gonna set up some mood</p>
        <label for="mood">Input </label>
        <input type="text" id="mood" />
        <div>
            <button onclick="getMood()">Get Mood</button>
        </div>
        <div>
            <button onclick="setMood()">Set Mood</button>
        </div>
    </body>

<script
  src="https://cdn.ethers.io/scripts/ethers-v4.min.js"
  type="text/javascript"
></script>
<script>

    window.ethereum.enable();
    var provider = new ethers.providers.Web3Provider(
        web3.currentProvider,
        "ropsten"
    );
    var MoodContractAddress = "0xed8Ce672751C1ab6382F24585648A4D983a3F35E";
    var MoodContractABI = [
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_mood",
				"type": "string"
			}
		],
		"name": "setMood",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getMood",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
];
    var MoodContract;
    var signer;
    provider.listAccounts().then((accounts) => {
    signer = provider.getSigner(accounts[0]);
    MoodContract = new ethers.Contract(
      MoodContractAddress,
      MoodContractABI,
      signer
    );
  });

  async function getMood() {
    getMoodPromise = MoodContract.getMood();
    var Mood = await getMoodPromise;
    console.log(Mood);
}

  async function setMood() {
   let mood = document.getElementById("mood").value;
   setMoodPromise = MoodContract.setMood(mood);
   await setMoodPromise;
}
    
  </script>
</html>








Mood.Sol -

// SPDX-License-Identifier:MIT
pragma solidity ^0.8.4;
contract MoodDiary{

    string mood;

    function setMood(string memory _mood) public
    {
            mood = _mood;
    }

    function getMood() public view returns(string memory)
    {
              return mood;
    }
}








