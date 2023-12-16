import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';
import { faShield } from '@fortawesome/free-solid-svg-icons';

export default function index(){
    return(
    <>
  <div className='flex flex-col justify-center items-center'>
    <div className='yo p-8 rounded-md flex flex-col text-xl justify-center items-center text-white'>
        <FontAwesomeIcon icon={faExclamationTriangle} size="5x" color="red" />
        <h1 className='text-2xl text-center'>Malacious</h1>
    </div>
    <div className='yo p-8 rounded-md flex flex-col text-xl justify-center items-center text-white'>
        <FontAwesomeIcon icon={faShield} size="5x" color="green" />
        <h1 className='text-2xl text-center'>Non-Malacious</h1>
    </div>
  </div>
  </>
    )
}