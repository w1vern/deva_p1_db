

from typing import Optional, Sequence
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.models.file import File
from deva_p1_db.models.note import Note


class NoteRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, text: str, file: File, start_time_code: float, end_time_code: float = 0) -> Optional[Note]:
        if end_time_code == 0:
            end_time_code = start_time_code
        note = Note(text=text, file_id=file.id,
                    start_time_code=start_time_code, end_time_code=end_time_code)
        self.session.add(note)
        await self.session.flush()
        return await self.get_by_id(note.id)

    async def get_by_id(self, note_id: UUID) -> Optional[Note]:
        stmt = select(Note).where(Note.id == note_id)
        return await self.session.scalar(stmt)

    async def get_by_file(self, file: File) -> Sequence[Note]:
        stmt = select(Note).where(Note.file_id == file.id)
        return (await self.session.scalars(stmt)).all()

    async def delete(self, note: Note) -> None:
        await self.session.delete(note)
        await self.session.flush()

    async def update(self,
                     note: Note,
                     new_text: str | None = None,
                     new_start_time_code: float | None = None,
                     new_end_time_code: float | None = None
                     ) -> None:
        if new_text is not None:
            note.text = new_text
        if new_start_time_code is not None:
            note.start_time_code = new_start_time_code
        if new_end_time_code is not None:
            note.end_time_code = new_end_time_code
        await self.session.flush()
        
        
