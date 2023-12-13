import Link from "next/link";
const Navbar=()=>{
    return(
        <div className="fixed flex w-screen justify-evenly gap-6 pt-5 text-lg  text-white pb-5">
            <Link href="/">
              <h1 className="  hover:text-[#34B3F1] ">Home</h1>
            </Link>
            <Link href="/blacklisteddomain">
              <h1 className="  hover:text-[#34B3F1]">Blacklisted domain</h1>
            </Link>
            <Link href="/whitelistdomain">
              <h1 className="  hover:text-[#34B3F1]">Whitelisted domain</h1>
            </Link>
            <Link href="/noofrequests">
              <h1 className="  hover:text-[#34B3F1]">No of Requests</h1>
            </Link>
        </div>
    )
}
export default Navbar;