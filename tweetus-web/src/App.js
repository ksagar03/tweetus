import {useEffect, useState} from "react" 
import logo from './logo.svg';
import './App.css';

//  this below function is coppied from homepage.html
function load_tweets(fetch_data) {   
  // this function will load the tweets from the database and prints them 
  // in the respective spaces in the home page of the tweetus. 
  const xhr = new XMLHttpRequest()
  const method = 'GET' //(CRUD operation) methods(for more information refer notes)
  const url = 'http://127.0.0.1:8000/api/tweet'
  const responseType = 'json'
  xhr.responseType = responseType
  xhr.open(method, url) // here we opening the url '/tweet' which links to tweet-list
  // (it is defined in views.py)
  xhr.onload = function () { 
    return (xhr.response,xhr.status)
    }
  xhr.onerror =(e)=>{
    console.log(e)
    fetch_data({"message":"An error occured"},400)
  }
    xhr.send()
  }

function App() {
  const [tweet,setTweet] = useState([])

  useEffect(() =>{ 
    const fetchdata= (response,status)=>{
      if (status === 200)
      {
      setTweet(response)
    }
    else{
      alert("an error occured on loading")
    }

  }
    load_tweets(fetchdata)
   },[])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {/* Edit <code>src/App.js</code> and save to reload. */}
          {tweet.map((tweet,index) =>{
            return  <li>{tweet.content}</li>   
          })}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
