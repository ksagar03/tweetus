import React from 'react'

const Forms = ({className}) => {
    const text_typed_inside_form= React.createRef() // this line provide the tweet typed by the user 
                                                            // inside the form 
    const handleonsubmit =(event)=>{
        event.preventDefault()
        // console.log(event)
       const newTweet=text_typed_inside_form.current.value
        console.log(newTweet)
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
    </div>

  )
}

export default Forms
