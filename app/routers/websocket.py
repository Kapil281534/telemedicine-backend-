from fastapi import APIRouter, WebSocket

router = APIRouter()

connected_doctors = set()

@router.websocket("/ws/doctor/{doctor_id}")
async def doctor_status(websocket: WebSocket, doctor_id: int):
    await websocket.accept()
    connected_doctors.add(doctor_id)
    try:
        while True:
            await websocket.receive_text()
    except:
        connected_doctors.remove(doctor_id)
        await websocket.close()
