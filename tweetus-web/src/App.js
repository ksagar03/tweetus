import logo from './logo.svg';
import './App.css';
import TweetListFetching from "./functioality/TweetListFetching";
import Forms from './components/Forms';
function App() {
  const newtweets=Forms.newTweet
  console.log(newtweets)
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <Forms styles={"col-5 mb-3"}  />
          {/* <TweetListFetching newTweets={newtweets} />  */}
          {/* this above tag will fetch data from the backend and each tweet will be printed
          in separate block */}
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
