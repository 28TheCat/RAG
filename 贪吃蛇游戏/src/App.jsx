import { useState, useEffect, useCallback, useRef } from 'react'

const BOARD_WIDTH = 20
const BOARD_HEIGHT = 20
const INITIAL_SNAKE = [{ x: 10, y: 10 }]
const INITIAL_FOOD = { x: 15, y: 15 }

function App() {
  const [snake, setSnake] = useState(INITIAL_SNAKE)
  const [food, setFood] = useState(INITIAL_FOOD)
  const [direction, setDirection] = useState({ x: 1, y: 0 })
  const [isGameOver, setIsGameOver] = useState(false)
  const [isPlaying, setIsPlaying] = useState(false)
  const [score, setScore] = useState(0)
  const gameLoopRef = useRef(null)

  const generateFood = useCallback(() => {
    let newFood
    do {
      newFood = {
        x: Math.floor(Math.random() * BOARD_WIDTH),
        y: Math.floor(Math.random() * BOARD_HEIGHT)
      }
    } while (snake.some(segment => segment.x === newFood.x && segment.y === newFood.y))
    setFood(newFood)
  }, [snake])

  const moveSnake = useCallback(() => {
    setSnake(prevSnake => {
      const head = {
        x: prevSnake[0].x + direction.x,
        y: prevSnake[0].y + direction.y
      }

      // 碰撞检测
      if (
        head.x < 0 ||
        head.x >= BOARD_WIDTH ||
        head.y < 0 ||
        head.y >= BOARD_HEIGHT ||
        prevSnake.some(segment => segment.x === head.x && segment.y === head.y)
      ) {
        setIsGameOver(true)
        setIsPlaying(false)
        return prevSnake
      }

      const newSnake = [head, ...prevSnake]

      // 检查是否吃到食物
      if (head.x === food.x && head.y === food.y) {
        setScore(prev => prev + 10)
        generateFood()
      } else {
        newSnake.pop()
      }

      return newSnake
    })
  }, [direction, food, generateFood])

  useEffect(() => {
    if (isPlaying && !isGameOver) {
      gameLoopRef.current = setInterval(moveSnake, 200)
    } else {
      if (gameLoopRef.current) {
        clearInterval(gameLoopRef.current)
      }
    }

    return () => {
      if (gameLoopRef.current) {
        clearInterval(gameLoopRef.current)
      }
    }
  }, [isPlaying, isGameOver, moveSnake])

  const handleKeyDown = useCallback((e) => {
    if (isGameOver) return

    switch (e.key) {
      case 'ArrowUp':
        if (direction.y !== 1) {
          setDirection({ x: 0, y: -1 })
        }
        break
      case 'ArrowDown':
        if (direction.y !== -1) {
          setDirection({ x: 0, y: 1 })
        }
        break
      case 'ArrowLeft':
        if (direction.x !== 1) {
          setDirection({ x: -1, y: 0 })
        }
        break
      case 'ArrowRight':
        if (direction.x !== -1) {
          setDirection({ x: 1, y: 0 })
        }
        break
      case ' ':
        setIsPlaying(prev => !prev)
        break
      default:
        break
    }
  }, [direction, isGameOver])

  useEffect(() => {
    window.addEventListener('keydown', handleKeyDown)
    return () => {
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [handleKeyDown])

  const resetGame = () => {
    setSnake(INITIAL_SNAKE)
    setFood(INITIAL_FOOD)
    setDirection({ x: 1, y: 0 })
    setIsGameOver(false)
    setIsPlaying(false)
    setScore(0)
  }

  const renderBoard = () => {
    const board = []
    for (let y = 0; y < BOARD_HEIGHT; y++) {
      for (let x = 0; x < BOARD_WIDTH; x++) {
        const isSnake = snake.some(segment => segment.x === x && segment.y === y)
        const isFood = food.x === x && food.y === y
        const isHead = snake.length > 0 && snake[0].x === x && snake[0].y === y

        board.push(
          <div
            key={`${x}-${y}`}
            className={`cell ${isSnake ? (isHead ? 'snake-head' : 'snake') : ''} ${isFood ? 'food' : ''}`}
          />
        )
      }
    }
    return board
  }

  return (
    <div className="app">
      <div className="game-container">
        <h1 className="title">贪吃蛇游戏</h1>
        
        <div className="info-bar">
          <div className="score">分数: {score}</div>
          <div className="controls">
            {!isPlaying ? (
              <button onClick={() => setIsPlaying(true)} className="btn">开始游戏</button>
            ) : (
              <button onClick={() => setIsPlaying(false)} className="btn">暂停</button>
            )}
            {isGameOver && (
              <button onClick={resetGame} className="btn btn-danger">重新开始</button>
            )}
          </div>
        </div>

        <div className="game-board">
          {renderBoard()}
        </div>

        {isGameOver && (
          <div className="game-over">
            <h2>游戏结束</h2>
            <p>最终得分: {score}</p>
            <button onClick={resetGame} className="btn btn-primary">再来一局</button>
          </div>
        )}

        <div className="instructions">
          <p>使用方向键控制蛇的移动</p>
          <p>按空格键开始/暂停游戏</p>
          <p>吃到食物得分，撞到墙壁或自己则游戏结束</p>
        </div>
      </div>
    </div>
  )
}

export default App
