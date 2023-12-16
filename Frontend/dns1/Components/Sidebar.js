
import Link from "next/link"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faHome } from '@fortawesome/free-solid-svg-icons';
import { faChartBar } from '@fortawesome/free-solid-svg-icons';
import { faInfoCircle } from '@fortawesome/free-solid-svg-icons';
const Sidebar=()=>{
    return(
        <div className={`fixed flex flex-col justify-evenly items-center border-r top-0  left-0 bottom-0 w-40
     `}>
        <Link href="/">
          <h1 className="text-white text-lg hover:text-blue-500"><FontAwesomeIcon icon={faHome} size="1x" />  Dashboard</h1>
        </Link>
        <Link href="/">
          <h1 className="text-white text-lg hover:text-blue-500"><FontAwesomeIcon icon={faChartBar} size="1x" />  Tables</h1>
        </Link>
        <Link href="/domaindetails">
          <h1 className="text-white text-lg hover:text-blue-500"><FontAwesomeIcon icon={faInfoCircle} size="1x" /> Domain Details</h1>
        </Link>
    </div>
    )
}
export default Sidebar;