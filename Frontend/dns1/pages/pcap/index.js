export default function Index(){
    return(
        <div className="flex flex-col gap-8">
        <h1 className="text-white text-xl">Lorem </h1>
        <div className="flex justify-center items-center">
        <label className="text-white text-lg"> Upload File: </label>
        <input type="file" className="text-black p-1 shadow-md shadow-black rounded-md " placeholder="Upload File"/>
        </div>
        </div>
    )
}