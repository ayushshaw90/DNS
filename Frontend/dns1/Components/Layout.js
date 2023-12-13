import Sidebar from './Sidebar'
const Layout = ({ children}) => {

    return (
        <div className={" w-screen " }>
            <Sidebar/>
            {children}
        </div>
    )
}

export default Layout