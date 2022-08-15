import logo from './logo.svg';
import './App.css';
import TweetListFetching from "./functioality/TweetListFetching";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <TweetListFetching /> 
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
