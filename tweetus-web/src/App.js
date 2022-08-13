import {useEffect, useState} from "react" 
import logo from './logo.svg';
import Tweets from "./components/Tweets";
import './App.css';

//  this below function is coppied from homepage.html
// function load_tweets(fetching_data) {   
//   // this function will load the tweets from the database and prints them 
//   // in the respective spaces in the home page of the tweetus. 
//   const xhr = new XMLHttpRequest()
//   const method = 'GET' //(CRUD operation) methods(for more information refer notes)
//   const url = 'http://localhost:8000/api/tweet/'
//   // the django  react server ports are different therefore to fetch data from django
//   // (database is linked to django)      
//   // we need to tell react to fetch data from that server(http://127.0.0.1:8000/api/tweet)
//                          /*
//                           Note:
//                               even after specifing the path to the react, it can't fetch data because
//                               django won't allow external server to interact with it 
//                               therefore to get access we need to specify or mention react server address 
//                               in allowed host in django settings
//                            */
//   const responseType = 'json'
//   xhr.responseType = responseType
//   xhr.open(method, url)   // here we opening the url '/tweet' which links to tweet-list
//   // (it is defined in views.py)
//   xhr.onload = function () { 
//     fetching_data(xhr.response,xhr.status)
//     }
//   xhr.onerror =(e)=>{
//     console.log(e)
//     fetching_data({"message":"An error occured"},400)
//   }
//     xhr.send()
//   }

function App() {
  const [tweets,setTweets] = useState([])
  const [errors,setErrors]=useState(null)

 
    const fetchdata= async ()=>{
      // console.log(response,status)
    //   if (status === 200)
      // {                                             # this is old way of doing it
    //   setTweets(response)                     here first we fetch data in xml format and then
    // }                                         we convert into json fromat
    // else{
    //   alert("an error occured on loading")
    // }
      //   

// using fetch function we can easily fetch data from the server and convert that data into jason format
// SYNTAX for fetch --> fetch("URL",'CRUD methods')

    //   const response= await fetch("http://localhost:8000/api/tweet/",{headers : { 
    //     'Content-Type': 'application/json',
    //     'Accept': 'application/json'
    // }})
    // const data = await response.json();
    // console.log(data)
    // setTweets(data)

    // we can also write above code like this
    // here we are using .then(after fetching the data what needs to be done next can be specified),
    //  .catch(used to catch some error) insted of using constants to specify

    const response= await fetch("http://localhost:8000/api/tweet/",{headers : { 
           'Content-Type': 'application/json',
           'Accept': 'application/json'
       }}).then(response =>{
        console.log(response)
        if (!response.ok){
          throw Error("Not able to fetch data from the server")  //
        } 
        return response.json()
      }).then(data =>{
        console.log(data)
        setTweets(data)
      }).catch(err =>{
          setErrors(err.message)
      })
  }
  useEffect(() =>{ 
    fetchdata()
   },[])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          {errors && <p>{errors}</p>}
          {/* Edit <code>src/App.js</code> and save to reload. */}
          {tweets.map((items,index) =>{
            return  <Tweets className='my-5 py-5 border bg-white text-dark' key={index} tweet={items}  />   
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
