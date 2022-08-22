import React, {useState} from 'react'
import TweetListFetching from '../functioality/TweetListFetching'

// const [newTweet, setNewTweet]= useState([])

const Forms = ({className}) => {
    const text_typed_inside_form= React.createRef() // this line provide the tweet typed by the user 
                                                            // inside the form 
    const [newTweet, setNewTweet]= useState([])
    const handleonsubmit =(event)=>{
        event.preventDefault()
        // console.log(event)
       const newTweet_typed=text_typed_inside_form.current.value
       let tempTweet=[...newTweet]
       tempTweet.unshift(
        {
          content: newTweet_typed,
          like: 12,
          id:1234
        }
       )
       setNewTweet(tempTweet)
      //  console.log(newTweet)
        text_typed_inside_form.current.value='' // after clicking on tweet btn it will clear the form
    }
  return (
    <div className={className}>
    <div  >
        <form onSubmit={handleonsubmit}>
            <textarea ref={text_typed_inside_form} className="form-control"  required={true} name="content" placeholder="type your tweet">
            </textarea>
            <button type='submit' className='btn btn-dark my-3' >Tweet</button>
        </form>
  
    </div>
    <TweetListFetching newTweet={newTweet}/>
    </div>

  )
}

export default Forms
