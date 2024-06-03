function solve(input) {
    class Song {
        constructor(typeList, name, time) {
            this.typeList = typeList;
            this.name = name;
            this.time = time;
        }
    }   
    let songsCollection = [];
    const numberOfSongs = input.shift();

    for (let i = 0; i < numberOfSongs; i++) {
        const [typeList, name, time] = input.shift().split('_');
        songsCollection.push(new Song(typeList, name, time));
    }

    type = input.shift()
    if (type === 'all') {
        for (const song of songsCollection) {
         console.log(song.name);
        }
    }else {
        for (const song of songsCollection) {
            if (type === song.typeList) {
            console.log(song.name);
            }
        } 
    }
}

solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']
    
    )